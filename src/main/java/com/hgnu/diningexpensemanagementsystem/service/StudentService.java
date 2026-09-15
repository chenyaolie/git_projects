package com.hgnu.diningexpensemanagementsystem.service;

import com.hgnu.diningexpensemanagementsystem.entity.StudentDEMS;

import java.math.BigDecimal;
import java.util.List;

public interface StudentService {
    StudentDEMS login(String studentId, String password);
    void register(StudentDEMS student);
    StudentDEMS getStudentById(String studentId);
    void updateStudent(StudentDEMS student);
    void deleteStudent(String studentId);
    List<StudentDEMS> getAllStudents();
    void updateBalance(String studentId, BigDecimal amount);
    void updatePassword(String studentId, String password);
    void updateIsLost(String studentId, Integer isLost);
    void resetPassword(String studentId);
}
