package com.hgnu.diningexpensemanagementsystem.mapper;

import com.hgnu.diningexpensemanagementsystem.entity.ConsumptionRecordDEMS;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.List;

@Mapper
public interface ConsumptionRecordMapper {
    void insert(ConsumptionRecordDEMS record);
    List<ConsumptionRecordDEMS> selectByStudentId(String studentId);
    List<ConsumptionRecordDEMS> selectByStaffIdAndDate(@Param("staffId") String staffId, @Param("date") String date);
    List<ConsumptionRecordDEMS> selectByDateRange(@Param("startDate") String startDate, @Param("endDate") String endDate);
    List<ConsumptionRecordDEMS> selectByStudentIdAndDateRange(@Param("studentId") String studentId, @Param("startDate") String startDate, @Param("endDate") String endDate);
    BigDecimal sumByStaffIdAndDate(@Param("staffId") String staffId, @Param("date") String date);
    BigDecimal sumByDate(String date);
    List<ConsumptionRecordDEMS> selectAllByConditions(@Param("studentId") String studentId, @Param("staffId") String staffId, @Param("startDate") String startDate, @Param("endDate") String endDate);
}
