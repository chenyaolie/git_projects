package com.hgnu.diningexpensemanagementsystem.service.impl;

import com.hgnu.diningexpensemanagementsystem.entity.ConsumptionRecordDEMS;
import com.hgnu.diningexpensemanagementsystem.entity.StudentDEMS;
import com.hgnu.diningexpensemanagementsystem.mapper.ConsumptionRecordMapper;
import com.hgnu.diningexpensemanagementsystem.mapper.StudentMapper;
import com.hgnu.diningexpensemanagementsystem.service.ConsumptionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.List;

@Service
public class ConsumptionServiceImpl implements ConsumptionService {

    @Autowired
    private ConsumptionRecordMapper consumptionRecordMapper;

    @Autowired
    private StudentMapper studentMapper;

    @Override
    public String consume(String studentId, String staffId, BigDecimal amount) {
        if (amount.compareTo(BigDecimal.ZERO) <= 0) {
            return "消费金额必须大于0";
        }
        StudentDEMS student = studentMapper.selectByStudentId(studentId);
        if (student == null) {
            return "学生不存在";
        }
        if (student.getIsLost() == 1) {
            return "饭卡已挂失，无法付款";
        }
        if (amount.compareTo(student.getBalance()) > 0) {
            return "余额不足";
        }
        studentMapper.updateBalance(studentId, student.getBalance().subtract(amount));

        ConsumptionRecordDEMS record = new ConsumptionRecordDEMS();
        record.setStudentId(studentId);
        record.setStaffId(staffId);
        record.setAmount(amount);
        record.setCreateTime(LocalDateTime.now());
        consumptionRecordMapper.insert(record);
        return "success";
    }

    @Override
    public List<ConsumptionRecordDEMS> getConsumptionByStudentId(String studentId) {
        return consumptionRecordMapper.selectByStudentId(studentId);
    }

    @Override
    public List<ConsumptionRecordDEMS> getTodayRecordsByStaffId(String staffId) {
        String today = LocalDate.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd"));
        return consumptionRecordMapper.selectByStaffIdAndDate(staffId, today);
    }

    @Override
    public BigDecimal getTodayTotalByStaffId(String staffId) {
        String today = LocalDate.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd"));
        if (staffId == null || staffId.trim().isEmpty()) {
            // staffId为空时，统计所有员工的今日消费总额
            return consumptionRecordMapper.sumByDate(today);
        }
        return consumptionRecordMapper.sumByStaffIdAndDate(staffId, today);
    }

    @Override
    public List<ConsumptionRecordDEMS> getRecordsByDateRange(String startDate, String endDate) {
        return consumptionRecordMapper.selectByDateRange(startDate + " 00:00:00", endDate + " 23:59:59");
    }

    @Override
    public List<ConsumptionRecordDEMS> getRecordsByStudentIdAndDateRange(String studentId, String startDate, String endDate) {
        return consumptionRecordMapper.selectByStudentIdAndDateRange(studentId, startDate + " 00:00:00", endDate + " 23:59:59");
    }

    @Override
    public List<ConsumptionRecordDEMS> getAllRecords(String studentId, String staffId, String startDate, String endDate) {
        String start = startDate != null && !startDate.isEmpty() ? startDate + " 00:00:00" : null;
        String end = endDate != null && !endDate.isEmpty() ? endDate + " 23:59:59" : null;
        return consumptionRecordMapper.selectAllByConditions(studentId, staffId, start, end);
    }
}
