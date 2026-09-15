package com.hgnu.diningexpensemanagementsystem.mapper;

import com.hgnu.diningexpensemanagementsystem.entity.RechargeRecordDEMS;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface RechargeRecordMapper {
    void insert(RechargeRecordDEMS record);
    List<RechargeRecordDEMS> selectByStudentId(String studentId);
    List<RechargeRecordDEMS> selectByDateRange(@Param("startDate") String startDate, @Param("endDate") String endDate);
    List<RechargeRecordDEMS> selectAllByConditions(@Param("studentId") String studentId, @Param("operatorId") String operatorId, @Param("startDate") String startDate, @Param("endDate") String endDate);
}
