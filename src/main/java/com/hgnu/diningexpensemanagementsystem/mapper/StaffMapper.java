package com.hgnu.diningexpensemanagementsystem.mapper;

import com.hgnu.diningexpensemanagementsystem.entity.StaffDEMS;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface StaffMapper {
    StaffDEMS selectByStaffId(String staffId);
    void insert(StaffDEMS staff);
    void update(StaffDEMS staff);
    void delete(String staffId);
    List<StaffDEMS> selectAll();
    void updatePassword(@Param("staffId") String staffId, @Param("password") String password);
}
