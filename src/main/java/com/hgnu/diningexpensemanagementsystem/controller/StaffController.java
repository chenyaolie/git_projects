package com.hgnu.diningexpensemanagementsystem.controller;

import com.hgnu.diningexpensemanagementsystem.entity.ConsumptionRecordDEMS;
import com.hgnu.diningexpensemanagementsystem.entity.StaffDEMS;
import com.hgnu.diningexpensemanagementsystem.entity.StudentDEMS;
import com.hgnu.diningexpensemanagementsystem.service.ConsumptionService;
import com.hgnu.diningexpensemanagementsystem.service.StaffService;
import com.hgnu.diningexpensemanagementsystem.service.StudentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import java.math.BigDecimal;
import java.util.List;

@Controller
@RequestMapping("/staff")
public class StaffController {

    @Autowired
    private StaffService staffService;

    @Autowired
    private StudentService studentService;

    @Autowired
    private ConsumptionService consumptionService;

    @GetMapping("/login")
    public String loginPage() {
        return "staff/login";
    }

    @PostMapping("/login")
    public String login(@RequestParam String staffId, @RequestParam String password, Model model) {
        StaffDEMS staff = staffService.login(staffId, password);
        if (staff != null) {
            return "redirect:/staff/index?staffId=" + staffId;
        }
        model.addAttribute("error", "工号或密码错误");
        return "staff/login";
    }

    @GetMapping("/logout")
    public String logout() {
        return "redirect:/staff/login";
    }

    @GetMapping("/index")
    public String index(@RequestParam String staffId, 
                       @RequestParam(required = false) String success,
                       Model model) {
        StaffDEMS staff = staffService.getStaffById(staffId);
        model.addAttribute("staff", staff);
        if (success != null && !success.isEmpty()) {
            model.addAttribute("success", success);
        }
        return "staff/index";
    }

    @GetMapping("/consume")
    public String consumePage(@RequestParam String staffId, 
                             @RequestParam(required = false) String studentId,
                             @RequestParam(required = false) String success,
                             @RequestParam(required = false) String error,
                             Model model) {
        model.addAttribute("staffId", staffId);
        if (studentId != null && !studentId.isEmpty()) {
            StudentDEMS student = studentService.getStudentById(studentId);
            model.addAttribute("student", student);
        }
        if (success != null && !success.isEmpty()) {
            model.addAttribute("success", success);
        }
        if (error != null && !error.isEmpty()) {
            model.addAttribute("error", error);
        }
        return "staff/consume";
    }

    @PostMapping("/consume/search")
    public String searchStudent(@RequestParam String staffId, @RequestParam String studentId, Model model) {
        return "redirect:/staff/consume?staffId=" + staffId + "&studentId=" + studentId;
    }

    @PostMapping("/consume/confirm")
    public String consume(@RequestParam String staffId, 
                         @RequestParam String studentId, 
                         @RequestParam BigDecimal amount,
                         Model model) {
        String result = consumptionService.consume(studentId, staffId, amount);
        if ("success".equals(result)) {
            // 重新获取学生信息以更新余额
            StudentDEMS student = studentService.getStudentById(studentId);
            model.addAttribute("staffId", staffId);
            model.addAttribute("student", student);
            model.addAttribute("success", "消费成功");
            return "staff/consume";
        } else {
            StudentDEMS student = studentService.getStudentById(studentId);
            model.addAttribute("staffId", staffId);
            model.addAttribute("student", student);
            model.addAttribute("error", result);
            return "staff/consume";
        }
    }

    @GetMapping("/today/records")
    public String todayRecords(@RequestParam String staffId, Model model) {
        List<ConsumptionRecordDEMS> records = consumptionService.getTodayRecordsByStaffId(staffId);
        BigDecimal total = consumptionService.getTodayTotalByStaffId(staffId);
        model.addAttribute("records", records);
        model.addAttribute("totalAmount", total);
        model.addAttribute("recordCount", records != null ? records.size() : 0);
        model.addAttribute("staffId", staffId);
        return "staff/today_records";
    }

    @GetMapping("/history/records")
    public String historyRecords(@RequestParam String staffId,
                                @RequestParam(required = false) String startDate,
                                @RequestParam(required = false) String endDate,
                                @RequestParam(required = false) String studentId,
                                Model model) {
        List<ConsumptionRecordDEMS> records;
        BigDecimal totalAmount = BigDecimal.ZERO;
        
        // 优先按学号查询（单独学号即可查询）
        if (studentId != null && !studentId.trim().isEmpty()) {
            records = consumptionService.getRecordsByStudentIdAndDateRange(studentId, 
                startDate != null && !startDate.isEmpty() ? startDate : "2000-01-01", 
                endDate != null && !endDate.isEmpty() ? endDate : "2100-12-31");
        } 
        // 按日期范围查询
        else if (startDate != null && !startDate.isEmpty() && endDate != null && !endDate.isEmpty()) {
            records = consumptionService.getRecordsByDateRange(startDate, endDate);
        } 
        // 查询所有记录
        else {
            records = consumptionService.getAllRecords(null, staffId, null, null);
        }
        
        // 计算总金额
        if (records != null && !records.isEmpty()) {
            for (ConsumptionRecordDEMS record : records) {
                if (record.getAmount() != null) {
                    totalAmount = totalAmount.add(record.getAmount());
                }
            }
        }
        
        model.addAttribute("records", records);
        model.addAttribute("totalAmount", totalAmount);
        model.addAttribute("staffId", staffId);
        model.addAttribute("studentId", studentId);
        model.addAttribute("startDate", startDate);
        model.addAttribute("endDate", endDate);
        return "staff/history_records";
    }

    @GetMapping("/password/change")
    public String changePasswordPage(@RequestParam String staffId, 
                                    @RequestParam(required = false) String error,
                                    @RequestParam(required = false) String success,
                                    Model model) {
        model.addAttribute("staffId", staffId);
        if (error != null && !error.isEmpty()) {
            model.addAttribute("error", error);
        }
        if (success != null && !success.isEmpty()) {
            model.addAttribute("success", success);
        }
        return "staff/change_password";
    }

    @PostMapping("/password/change")
    public String changePassword(@RequestParam String staffId, 
                                @RequestParam String oldPassword, 
                                @RequestParam String newPassword,
                                @RequestParam String confirmPassword,
                                RedirectAttributes redirectAttributes) {
        if (!newPassword.equals(confirmPassword)) {
            redirectAttributes.addFlashAttribute("error", "两次输入的密码不一致");
            return "redirect:/staff/password/change?staffId=" + staffId;
        }
        StaffDEMS staff = staffService.login(staffId, oldPassword);
        if (staff != null) {
            staffService.updatePassword(staffId, newPassword);
            redirectAttributes.addFlashAttribute("success", "密码修改成功");
            return "redirect:/staff/password/change?staffId=" + staffId;
        }
        redirectAttributes.addFlashAttribute("error", "原密码错误");
        return "redirect:/staff/password/change?staffId=" + staffId;
    }
}
