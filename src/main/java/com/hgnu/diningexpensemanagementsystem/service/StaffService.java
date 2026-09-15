package com.hgnu.diningexpensemanagementsystem.service;

import com.hgnu.diningexpensemanagementsystem.entity.StaffDEMS;

import java.util.List;

public interface StaffService {
    StaffDEMS login(String staffId, String password);
    StaffDEMS getStaffById(String staffId);
    void addStaff(StaffDEMS staff);
    void updateStaff(StaffDEMS staff);
    void deleteStaff(String staffId);
    List<StaffDEMS> getAllStaff();
    void updatePassword(String staffId, String password);
}
