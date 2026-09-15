package com.hgnu.diningexpensemanagementsystem.service.impl;

import com.hgnu.diningexpensemanagementsystem.entity.StudentDEMS;
import com.hgnu.diningexpensemanagementsystem.mapper.StudentMapper;
import com.hgnu.diningexpensemanagementsystem.service.StudentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.util.List;

@Service
public class StudentServiceImpl implements StudentService {

    @Autowired
    private StudentMapper studentMapper;

    @Override
    public StudentDEMS login(String studentId, String password) {
        StudentDEMS student = studentMapper.selectByStudentId(studentId);
        if (student != null && password.equals(student.getPassword())) {
            return student;
        }
        return null;
    }

    @Override
    public void register(StudentDEMS student) {
        student.setBalance(BigDecimal.ZERO);
        student.setIsLost(0);
        studentMapper.insert(student);
    }

    @Override
    public StudentDEMS getStudentById(String studentId) {
        return studentMapper.selectByStudentId(studentId);
    }

    @Override
    public void updateStudent(StudentDEMS student) {
        studentMapper.update(student);
    }

    @Override
    public void deleteStudent(String studentId) {
        studentMapper.delete(studentId);
    }

    @Override
    public List<StudentDEMS> getAllStudents() {
        return studentMapper.selectAll();
    }

    @Override
    public void updateBalance(String studentId, BigDecimal amount) {
        studentMapper.updateBalance(studentId, amount);
    }

    @Override
    public void updatePassword(String studentId, String password) {
        studentMapper.updatePassword(studentId, password);
    }

    @Override
    public void updateIsLost(String studentId, Integer isLost) {
        studentMapper.updateIsLost(studentId, isLost);
    }

    @Override
    public void resetPassword(String studentId) {
        studentMapper.updatePassword(studentId, "123456");
    }
}
