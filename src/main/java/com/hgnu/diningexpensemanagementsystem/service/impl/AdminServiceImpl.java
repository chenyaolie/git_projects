package com.hgnu.diningexpensemanagementsystem.service.impl;

import com.hgnu.diningexpensemanagementsystem.entity.AdminDEMS;
import com.hgnu.diningexpensemanagementsystem.mapper.AdminMapper;
import com.hgnu.diningexpensemanagementsystem.service.AdminService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class AdminServiceImpl implements AdminService {

    @Autowired
    private AdminMapper adminMapper;

    @Override
    public AdminDEMS login(String adminId, String password) {
        AdminDEMS admin = adminMapper.selectByAdminId(adminId);
        if (admin != null && password.equals(admin.getPassword())) {
            return admin;
        }
        return null;
    }

    @Override
    public AdminDEMS getAdminById(String adminId) {
        return adminMapper.selectByAdminId(adminId);
    }

    @Override
    public void updatePassword(String adminId, String password) {
        adminMapper.updatePassword(adminId, password);
    }
}
