package com.hgnu.diningexpensemanagementsystem.mapper;

import com.hgnu.diningexpensemanagementsystem.entity.RechargeApplicationDEMS;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface RechargeApplicationMapper {
    void insert(RechargeApplicationDEMS application);
    List<RechargeApplicationDEMS> selectByStudentId(String studentId);
    List<RechargeApplicationDEMS> selectByStatus(Integer status);
    RechargeApplicationDEMS selectByApplicationId(Long applicationId);
    void updateStatus(@Param("applicationId") Long applicationId, @Param("status") Integer status, @Param("adminId") String adminId);
    List<RechargeApplicationDEMS> selectAll();
}
