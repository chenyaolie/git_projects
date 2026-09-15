package com.hgnu.diningexpensemanagementsystem.mapper;

import com.hgnu.diningexpensemanagementsystem.entity.AdminDEMS;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

@Mapper
public interface AdminMapper {
    AdminDEMS selectByAdminId(String adminId);
    void updatePassword(@Param("adminId") String adminId, @Param("password") String password);
}
