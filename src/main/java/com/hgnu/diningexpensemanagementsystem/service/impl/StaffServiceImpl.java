package com.hgnu.diningexpensemanagementsystem.service.impl;

import com.hgnu.diningexpensemanagementsystem.entity.StaffDEMS;
import com.hgnu.diningexpensemanagementsystem.mapper.StaffMapper;
import com.hgnu.diningexpensemanagementsystem.service.StaffService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class StaffServiceImpl implements StaffService {

    @Autowired
    private StaffMapper staffMapper;

    @Override
    public StaffDEMS login(String staffId, String password) {
        StaffDEMS staff = staffMapper.selectByStaffId(staffId);
        if (staff != null && password.equals(staff.getPassword())) {
            return staff;
        }
        return null;
    }

    @Override
    public StaffDEMS getStaffById(String staffId) {
        return staffMapper.selectByStaffId(staffId);
    }

    @Override
    public void addStaff(StaffDEMS staff) {
        staffMapper.insert(staff);
    }

    @Override
    public void updateStaff(StaffDEMS staff) {
        staffMapper.update(staff);
    }

    @Override
    public void deleteStaff(String staffId) {
        staffMapper.delete(staffId);
    }

    @Override
    public List<StaffDEMS> getAllStaff() {
        return staffMapper.selectAll();
    }

    @Override
    public void updatePassword(String staffId, String password) {
        staffMapper.updatePassword(staffId, password);
    }
}
