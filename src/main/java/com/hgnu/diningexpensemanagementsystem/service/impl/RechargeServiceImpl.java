package com.hgnu.diningexpensemanagementsystem.service.impl;

import com.hgnu.diningexpensemanagementsystem.entity.RechargeApplicationDEMS;
import com.hgnu.diningexpensemanagementsystem.entity.RechargeRecordDEMS;
import com.hgnu.diningexpensemanagementsystem.mapper.RechargeApplicationMapper;
import com.hgnu.diningexpensemanagementsystem.mapper.RechargeRecordMapper;
import com.hgnu.diningexpensemanagementsystem.mapper.StudentMapper;
import com.hgnu.diningexpensemanagementsystem.service.RechargeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.math.BigDecimal;
import java.util.List;

@Service
public class RechargeServiceImpl implements RechargeService {

    @Autowired
    private RechargeApplicationMapper rechargeApplicationMapper;

    @Autowired
    private RechargeRecordMapper rechargeRecordMapper;

    @Autowired
    private StudentMapper studentMapper;

    @Override
    public void applyRecharge(String studentId, BigDecimal amount) {
        RechargeApplicationDEMS application = new RechargeApplicationDEMS();
        application.setStudentId(studentId);
        application.setAmount(amount);
        application.setStatus(0);
        rechargeApplicationMapper.insert(application);
    }

    @Override
    public List<RechargeApplicationDEMS> getApplicationsByStudentId(String studentId) {
        return rechargeApplicationMapper.selectByStudentId(studentId);
    }

    @Override
    public List<RechargeApplicationDEMS> getApplicationsByStatus(Integer status) {
        return rechargeApplicationMapper.selectByStatus(status);
    }

    @Override
    @Transactional
    public void auditApplication(Long applicationId, Integer status, String adminId) {
        RechargeApplicationDEMS application = rechargeApplicationMapper.selectByApplicationId(applicationId);
        if (application == null) {
            throw new RuntimeException("充值申请不存在");
        }
        if (application.getStatus() != 0) {
            throw new RuntimeException("该申请已审核，不能重复审核");
        }
        rechargeApplicationMapper.updateStatus(applicationId, status, adminId);
        
        if (status == 1) {
            studentMapper.updateBalance(application.getStudentId(), application.getAmount());
            
            RechargeRecordDEMS record = new RechargeRecordDEMS();
            record.setStudentId(application.getStudentId());
            record.setAmount(application.getAmount());
            record.setType(0);
            record.setOperatorId(adminId);
            rechargeRecordMapper.insert(record);
        }
    }

    @Override
    @Transactional
    public void directRecharge(String studentId, BigDecimal amount, String adminId) {
        studentMapper.updateBalance(studentId, amount);
        
        RechargeRecordDEMS record = new RechargeRecordDEMS();
        record.setStudentId(studentId);
        record.setAmount(amount);
        record.setType(1);
        record.setOperatorId(adminId);
        rechargeRecordMapper.insert(record);
    }

    @Override
    public List<RechargeRecordDEMS> getRechargeRecordsByStudentId(String studentId) {
        return rechargeRecordMapper.selectByStudentId(studentId);
    }

    @Override
    public List<RechargeRecordDEMS> getAllRechargeRecords(String studentId, String operatorId, String startDate, String endDate) {
        String start = startDate != null && !startDate.isEmpty() ? startDate + " 00:00:00" : null;
        String end = endDate != null && !endDate.isEmpty() ? endDate + " 23:59:59" : null;
        return rechargeRecordMapper.selectAllByConditions(studentId, operatorId, start, end);
    }

    @Override
    public List<RechargeApplicationDEMS> getAllApplications() {
        return rechargeApplicationMapper.selectAll();
    }
}
