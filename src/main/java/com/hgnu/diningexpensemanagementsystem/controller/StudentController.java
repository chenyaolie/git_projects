package com.hgnu.diningexpensemanagementsystem.controller;

import com.hgnu.diningexpensemanagementsystem.entity.ConsumptionRecordDEMS;
import com.hgnu.diningexpensemanagementsystem.entity.RechargeApplicationDEMS;
import com.hgnu.diningexpensemanagementsystem.entity.RechargeRecordDEMS;
import com.hgnu.diningexpensemanagementsystem.entity.StudentDEMS;
import com.hgnu.diningexpensemanagementsystem.service.ConsumptionService;
import com.hgnu.diningexpensemanagementsystem.service.RechargeService;
import com.hgnu.diningexpensemanagementsystem.service.StudentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import java.math.BigDecimal;
import java.util.List;

@Controller
@RequestMapping("/student")
public class StudentController {

    @Autowired
    private StudentService studentService;

    @Autowired
    private ConsumptionService consumptionService;

    @Autowired
    private RechargeService rechargeService;

    @GetMapping("/login")
    public String loginPage() {
        return "student/login";
    }

    @PostMapping("/login")
    public String login(@RequestParam String studentId, @RequestParam String password, Model model) {
        StudentDEMS student = studentService.login(studentId, password);
        if (student != null) {
            return "redirect:/student/index?studentId=" + studentId;
        }
        model.addAttribute("error", "学号或密码错误");
        return "student/login";
    }

    @GetMapping("/logout")
    public String logout() {
        return "redirect:/student/login";
    }

    @GetMapping("/register")
    public String registerPage() {
        return "student/register";
    }

    @PostMapping("/register")
    public String register(@ModelAttribute StudentDEMS student, Model model) {
        try {
            studentService.register(student);
            return "redirect:/student/login";
        } catch (Exception e) {
            model.addAttribute("error", "注册失败，学号已存在");
            return "student/register";
        }
    }

    @GetMapping("/index")
    public String index(@RequestParam String studentId, 
                       @RequestParam(required = false) String success,
                       Model model) {
        StudentDEMS student = studentService.getStudentById(studentId);
        model.addAttribute("student", student);
        if (success != null && !success.isEmpty()) {
            model.addAttribute("success", success);
        }
        return "student/index";
    }

    @GetMapping("/profile")
    public String profile(@RequestParam String studentId, Model model) {
        StudentDEMS student = studentService.getStudentById(studentId);
        model.addAttribute("student", student);
        return "student/profile";
    }

    @GetMapping("/recharge/apply")
    public String rechargeApplyPage(@RequestParam String studentId, 
                                   @RequestParam(required = false) String success,
                                   Model model) {
        model.addAttribute("studentId", studentId);
        if (success != null && !success.isEmpty()) {
            model.addAttribute("success", success);
        }
        return "student/recharge_apply";
    }

    @PostMapping("/recharge/apply")
    public String rechargeApply(@RequestParam String studentId, @RequestParam BigDecimal amount, RedirectAttributes redirectAttributes) {
        rechargeService.applyRecharge(studentId, amount);
        redirectAttributes.addFlashAttribute("success", "充值申请已提交，等待审核");
        return "redirect:/student/recharge/apply?studentId=" + studentId;
    }

    @GetMapping("/recharge/records")
    public String rechargeRecords(@RequestParam String studentId, Model model) {
        List<RechargeApplicationDEMS> applications = rechargeService.getApplicationsByStudentId(studentId);
        List<RechargeRecordDEMS> records = rechargeService.getRechargeRecordsByStudentId(studentId);
        model.addAttribute("applications", applications);
        model.addAttribute("records", records);
        model.addAttribute("studentId", studentId);
        return "student/recharge_records";
    }

    @GetMapping("/consumption/records")
    public String consumptionRecords(@RequestParam String studentId, 
                                    @RequestParam(required = false) String startDate,
                                    @RequestParam(required = false) String endDate,
                                    Model model) {
        List<ConsumptionRecordDEMS> records;
        if (startDate != null && endDate != null) {
            records = consumptionService.getRecordsByStudentIdAndDateRange(studentId, startDate, endDate);
        } else {
            records = consumptionService.getConsumptionByStudentId(studentId);
        }
        model.addAttribute("records", records);
        model.addAttribute("studentId", studentId);
        return "student/consumption_records";
    }

    @GetMapping("/password/change")
    public String changePasswordPage(@RequestParam String studentId, 
                                    @RequestParam(required = false) String error,
                                    @RequestParam(required = false) String success,
                                    Model model) {
        model.addAttribute("studentId", studentId);
        if (error != null && !error.isEmpty()) {
            model.addAttribute("error", error);
        }
        if (success != null && !success.isEmpty()) {
            model.addAttribute("success", success);
        }
        return "student/change_password";
    }

    @PostMapping("/password/change")
    public String changePassword(@RequestParam String studentId,
                                @RequestParam String oldPassword,
                                @RequestParam String newPassword,
                                @RequestParam String confirmPassword,
                                RedirectAttributes redirectAttributes) {
        if (!newPassword.equals(confirmPassword)) {
            redirectAttributes.addFlashAttribute("error", "两次输入的密码不一致");
            return "redirect:/student/password/change?studentId=" + studentId;
        }
        StudentDEMS student = studentService.login(studentId, oldPassword);
        if (student != null) {
            studentService.updatePassword(studentId, newPassword);
            redirectAttributes.addFlashAttribute("success", "密码修改成功");
            return "redirect:/student/password/change?studentId=" + studentId;
        }
        redirectAttributes.addFlashAttribute("error", "原密码错误");
        return "redirect:/student/password/change?studentId=" + studentId;
    }

    @PostMapping("/lost")
    public String lost(@RequestParam String studentId, RedirectAttributes redirectAttributes) {
        studentService.updateIsLost(studentId, 1);
        redirectAttributes.addFlashAttribute("success", "饭卡已挂失");
        return "redirect:/student/index?studentId=" + studentId;
    }

    @PostMapping("/unlost")
    public String unlost(@RequestParam String studentId, RedirectAttributes redirectAttributes) {
        studentService.updateIsLost(studentId, 0);
        redirectAttributes.addFlashAttribute("success", "饭卡已解除挂失");
        return "redirect:/student/index?studentId=" + studentId;
    }
}
