package com.hgnu.diningexpensemanagementsystem.service;

import com.hgnu.diningexpensemanagementsystem.entity.RechargeApplicationDEMS;
import com.hgnu.diningexpensemanagementsystem.entity.RechargeRecordDEMS;

import java.math.BigDecimal;
import java.util.List;

public interface RechargeService {
    void applyRecharge(String studentId, BigDecimal amount);
    List<RechargeApplicationDEMS> getApplicationsByStudentId(String studentId);
    List<RechargeApplicationDEMS> getApplicationsByStatus(Integer status);
    void auditApplication(Long applicationId, Integer status, String adminId);
    void directRecharge(String studentId, BigDecimal amount, String adminId);
    List<RechargeRecordDEMS> getRechargeRecordsByStudentId(String studentId);
    List<RechargeRecordDEMS> getAllRechargeRecords(String studentId, String operatorId, String startDate, String endDate);
    List<RechargeApplicationDEMS> getAllApplications();
}
