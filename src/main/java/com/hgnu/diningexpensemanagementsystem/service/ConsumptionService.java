package com.hgnu.diningexpensemanagementsystem.service;

import com.hgnu.diningexpensemanagementsystem.entity.ConsumptionRecordDEMS;

import java.math.BigDecimal;
import java.util.List;

public interface ConsumptionService {
    String consume(String studentId, String staffId, BigDecimal amount);
    List<ConsumptionRecordDEMS> getConsumptionByStudentId(String studentId);
    List<ConsumptionRecordDEMS> getTodayRecordsByStaffId(String staffId);
    BigDecimal getTodayTotalByStaffId(String staffId);
    List<ConsumptionRecordDEMS> getRecordsByDateRange(String startDate, String endDate);
    List<ConsumptionRecordDEMS> getRecordsByStudentIdAndDateRange(String studentId, String startDate, String endDate);
    List<ConsumptionRecordDEMS> getAllRecords(String studentId, String staffId, String startDate, String endDate);
}
