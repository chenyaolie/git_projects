package com.hgnu.diningexpensemanagementsystem.mapper;

import com.hgnu.diningexpensemanagementsystem.entity.StudentDEMS;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.math.BigDecimal;
import java.util.List;

@Mapper
public interface StudentMapper {
    StudentDEMS selectByStudentId(String studentId);
    void insert(StudentDEMS student);
    void update(StudentDEMS student);
    void delete(String studentId);
    List<StudentDEMS> selectAll();
    void updateBalance(@Param("studentId") String studentId, @Param("amount") BigDecimal amount);
    void updatePassword(@Param("studentId") String studentId, @Param("password") String password);
    void updateIsLost(@Param("studentId") String studentId, @Param("isLost") Integer isLost);
}
