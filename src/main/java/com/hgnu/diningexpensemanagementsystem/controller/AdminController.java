package com.hgnu.diningexpensemanagementsystem.controller;

import com.hgnu.diningexpensemanagementsystem.entity.*;
import com.hgnu.diningexpensemanagementsystem.service.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.List;

@Controller
@RequestMapping("/admin")
public class AdminController {

    @Autowired
    private AdminService adminService;

    @Autowired
    private StudentService studentService;

    @Autowired
    private StaffService staffService;

    @Autowired
    private RechargeService rechargeService;

    @Autowired
    private ConsumptionService consumptionService;

    @GetMapping("/login")
    public String loginPage() {
        return "admin/login";
    }

    @PostMapping("/login")
    public String login(@RequestParam String adminId, @RequestParam String password, Model model) {
        AdminDEMS admin = adminService.login(adminId, password);
        if (admin != null) {
            return "redirect:/admin/index?adminId=" + adminId;
        }
        model.addAttribute("error", "管理员编号或密码错误");
        return "admin/login";
    }

    @GetMapping("/index")
    public String index(@RequestParam String adminId, 
                       @RequestParam(required = false) String success,
                       Model model) {
        AdminDEMS admin = adminService.getAdminById(adminId);
        if (admin == null) {
            return "redirect:/admin/login";
        }
        String today = LocalDate.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd"));
        BigDecimal todayRevenue = consumptionService.getTodayTotalByStaffId(null);
        List<StudentDEMS> students = studentService.getAllStudents();
        List<StaffDEMS> staffList = staffService.getAllStaff();
        List<RechargeApplicationDEMS> pendingApplications = rechargeService.getApplicationsByStatus(0);
        
        model.addAttribute("admin", admin);
        model.addAttribute("todayRevenue", todayRevenue);
        model.addAttribute("studentCount", students.size());
        model.addAttribute("staffCount", staffList.size());
        model.addAttribute("pendingCount", pendingApplications.size());
        if (success != null && !success.isEmpty()) {
            model.addAttribute("success", success);
        }
        return "admin/index";
    }

    @GetMapping("/logout")
    public String logout() {
        return "redirect:/admin/login";
    }

    @GetMapping("/password/change")
    public String changePasswordPage(@RequestParam String adminId, 
                                    @RequestParam(required = false) String error,
                                    @RequestParam(required = false) String success,
                                    Model model) {
        model.addAttribute("adminId", adminId);
        if (error != null && !error.isEmpty()) {
            model.addAttribute("error", error);
        }
        if (success != null && !success.isEmpty()) {
            model.addAttribute("success", success);
        }
        return "admin/change_password";
    }

    @PostMapping("/password/change")
    public String changePassword(@RequestParam String adminId, 
                                @RequestParam String oldPassword, 
                                @RequestParam String newPassword,
                                @RequestParam String confirmPassword,
                                Model model) {
        if (!newPassword.equals(confirmPassword)) {
            return "redirect:/admin/password/change?adminId=" + adminId + "&error=两次输入的密码不一致";
        }
        AdminDEMS admin = adminService.login(adminId, oldPassword);
        if (admin != null) {
            adminService.updatePassword(adminId, newPassword);
            return "redirect:/admin/password/change?adminId=" + adminId + "&success=密码修改成功";
        }
        return "redirect:/admin/password/change?adminId=" + adminId + "&error=原密码错误";
    }

    @GetMapping("/student/list")
    public String studentList(@RequestParam String adminId, Model model) {
        List<StudentDEMS> students = studentService.getAllStudents();
        model.addAttribute("students", students);
        model.addAttribute("adminId", adminId);
        return "admin/student_list";
    }

    @GetMapping("/student/add")
    public String studentAddPage(@RequestParam String adminId, Model model) {
        model.addAttribute("adminId", adminId);
        return "admin/student_add";
    }

    @PostMapping("/student/add")
    public String studentAdd(@RequestParam String adminId, @ModelAttribute StudentDEMS student, Model model) {
        try {
            studentService.register(student);
            return "redirect:/admin/student/list?adminId=" + adminId;
        } catch (Exception e) {
            model.addAttribute("error", "添加失败，学号已存在");
            model.addAttribute("adminId", adminId);
            return "admin/student_add";
        }
    }

    @GetMapping("/student/edit")
    public String studentEditPage(@RequestParam String adminId, @RequestParam String studentId, Model model) {
        StudentDEMS student = studentService.getStudentById(studentId);
        model.addAttribute("student", student);
        model.addAttribute("adminId", adminId);
        return "admin/student_edit";
    }

    @PostMapping("/student/edit")
    public String studentEdit(@RequestParam String adminId, @ModelAttribute StudentDEMS student, Model model) {
        studentService.updateStudent(student);
        return "redirect:/admin/student/list?adminId=" + adminId;
    }

    @GetMapping("/student/delete")
    public String studentDelete(@RequestParam String adminId, @RequestParam String studentId) {
        studentService.deleteStudent(studentId);
        return "redirect:/admin/student/list?adminId=" + adminId;
    }

    @GetMapping("/student/resetPassword")
    public String studentResetPassword(@RequestParam String adminId, @RequestParam String studentId) {
        studentService.resetPassword(studentId);
        return "redirect:/admin/student/list?adminId=" + adminId;
    }

    @GetMapping("/student/adjustBalance")
    public String studentAdjustBalancePage(@RequestParam String adminId, 
                                          @RequestParam String studentId,
                                          @RequestParam(required = false) String success,
                                          Model model) {
        StudentDEMS student = studentService.getStudentById(studentId);
        model.addAttribute("student", student);
        model.addAttribute("adminId", adminId);
        if (success != null && !success.isEmpty()) {
            model.addAttribute("success", success);
        }
        return "admin/student_adjust_balance";
    }

    @PostMapping("/student/adjustBalance")
    public String studentAdjustBalance(@RequestParam String adminId, 
                                      @RequestParam String studentId, 
                                      @RequestParam BigDecimal amount,
                                      Model model) {
        studentService.updateBalance(studentId, amount);
        // 重新获取学生信息以更新余额
        StudentDEMS student = studentService.getStudentById(studentId);
        model.addAttribute("student", student);
        model.addAttribute("adminId", adminId);
        model.addAttribute("success", "余额调整成功");
        return "admin/student_adjust_balance";
    }

    @GetMapping("/staff/list")
    public String staffList(@RequestParam String adminId, Model model) {
        List<StaffDEMS> staffList = staffService.getAllStaff();
        model.addAttribute("staffList", staffList);
        model.addAttribute("adminId", adminId);
        return "admin/staff_list";
    }

    @GetMapping("/staff/add")
    public String staffAddPage(@RequestParam String adminId, Model model) {
        model.addAttribute("adminId", adminId);
        return "admin/staff_add";
    }

    @PostMapping("/staff/add")
    public String staffAdd(@RequestParam String adminId, @ModelAttribute StaffDEMS staff, Model model) {
        try {
            staffService.addStaff(staff);
            return "redirect:/admin/staff/list?adminId=" + adminId;
        } catch (Exception e) {
            model.addAttribute("error", "添加失败，员工编号已存在");
            model.addAttribute("adminId", adminId);
            return "admin/staff_add";
        }
    }

    @GetMapping("/staff/edit")
    public String staffEditPage(@RequestParam String adminId, @RequestParam String staffId, Model model) {
        StaffDEMS staff = staffService.getStaffById(staffId);
        model.addAttribute("staff", staff);
        model.addAttribute("adminId", adminId);
        return "admin/staff_edit";
    }

    @PostMapping("/staff/edit")
    public String staffEdit(@RequestParam String adminId, @ModelAttribute StaffDEMS staff, Model model) {
        staffService.updateStaff(staff);
        return "redirect:/admin/staff/list?adminId=" + adminId;
    }

    @GetMapping("/staff/delete")
    public String staffDelete(@RequestParam String adminId, @RequestParam String staffId) {
        staffService.deleteStaff(staffId);
        return "redirect:/admin/staff/list?adminId=" + adminId;
    }

    @GetMapping("/recharge/applications")
    public String rechargeApplications(@RequestParam String adminId, 
                                      @RequestParam(required = false) Integer status,
                                      Model model) {
        List<RechargeApplicationDEMS> applications;
        if (status != null) {
            applications = rechargeService.getApplicationsByStatus(status);
        } else {
            applications = rechargeService.getAllApplications();
        }
        model.addAttribute("applications", applications);
        model.addAttribute("adminId", adminId);
        return "admin/recharge_applications";
    }

    @PostMapping("/recharge/audit")
    public String auditRecharge(@RequestParam String adminId, 
                               @RequestParam Long applicationId, 
                               @RequestParam Integer status) {
        rechargeService.auditApplication(applicationId, status, adminId);
        return "redirect:/admin/recharge/applications?adminId=" + adminId;
    }

    @GetMapping("/recharge/direct")
    public String directRechargePage(@RequestParam String adminId, 
                                    @RequestParam(required = false) String studentId,
                                    @RequestParam(required = false) String success,
                                    Model model) {
        model.addAttribute("adminId", adminId);
        if (studentId != null && !studentId.isEmpty()) {
            StudentDEMS student = studentService.getStudentById(studentId);
            model.addAttribute("student", student);
        }
        if (success != null && !success.isEmpty()) {
            model.addAttribute("success", success);
        }
        return "admin/recharge_direct";
    }

    @PostMapping("/recharge/direct/search")
    public String searchStudentForRecharge(@RequestParam String adminId, @RequestParam String studentId, Model model) {
        return "redirect:/admin/recharge/direct?adminId=" + adminId + "&studentId=" + studentId;
    }

    @PostMapping("/recharge/direct/confirm")
    public String directRecharge(@RequestParam String adminId, 
                                @RequestParam String studentId, 
                                @RequestParam BigDecimal amount,
                                Model model) {
        rechargeService.directRecharge(studentId, amount, adminId);
        return "redirect:/admin/recharge/direct?adminId=" + adminId + "&studentId=" + studentId + "&success=充值成功";
    }

    @GetMapping("/consumption/records")
    public String consumptionRecords(@RequestParam String adminId,
                                    @RequestParam(required = false) String studentId,
                                    @RequestParam(required = false) String staffId,
                                    @RequestParam(required = false) String startDate,
                                    @RequestParam(required = false) String endDate,
                                    Model model) {
        // 处理空字符串参数
        String stuId = (studentId != null && !studentId.trim().isEmpty()) ? studentId : null;
        String stfId = (staffId != null && !staffId.trim().isEmpty()) ? staffId : null;
        String sDate = (startDate != null && !startDate.isEmpty()) ? startDate : null;
        String eDate = (endDate != null && !endDate.isEmpty()) ? endDate : null;
        
        List<ConsumptionRecordDEMS> records = consumptionService.getAllRecords(stuId, stfId, sDate, eDate);
        model.addAttribute("records", records);
        model.addAttribute("adminId", adminId);
        model.addAttribute("studentId", studentId);
        model.addAttribute("staffId", staffId);
        model.addAttribute("startDate", startDate);
        model.addAttribute("endDate", endDate);
        return "admin/consumption_records";
    }

    @GetMapping("/recharge/records")
    public String rechargeRecords(@RequestParam String adminId,
                                 @RequestParam(required = false) String studentId,
                                 @RequestParam(required = false) String operatorId,
                                 @RequestParam(required = false) String startDate,
                                 @RequestParam(required = false) String endDate,
                                 Model model) {
        // 处理空字符串参数
        String stuId = (studentId != null && !studentId.trim().isEmpty()) ? studentId : null;
        String opId = (operatorId != null && !operatorId.trim().isEmpty()) ? operatorId : null;
        String sDate = (startDate != null && !startDate.isEmpty()) ? startDate : null;
        String eDate = (endDate != null && !endDate.isEmpty()) ? endDate : null;
        
        List<RechargeRecordDEMS> records = rechargeService.getAllRechargeRecords(stuId, opId, sDate, eDate);
        model.addAttribute("records", records);
        model.addAttribute("adminId", adminId);
        model.addAttribute("studentId", studentId);
        model.addAttribute("operatorId", operatorId);
        model.addAttribute("startDate", startDate);
        model.addAttribute("endDate", endDate);
        return "admin/recharge_records";
    }

    @GetMapping("/statistics")
    public String statistics(@RequestParam String adminId, Model model) {
        BigDecimal todayRevenue = consumptionService.getTodayTotalByStaffId(null);
        int studentCount = studentService.getAllStudents().size();
        int staffCount = staffService.getAllStaff().size();
        int pendingCount = rechargeService.getApplicationsByStatus(0).size();
        
        model.addAttribute("todayRevenue", todayRevenue);
        model.addAttribute("studentCount", studentCount);
        model.addAttribute("staffCount", staffCount);
        model.addAttribute("pendingCount", pendingCount);
        model.addAttribute("adminId", adminId);
        return "admin/statistics";
    }
}
