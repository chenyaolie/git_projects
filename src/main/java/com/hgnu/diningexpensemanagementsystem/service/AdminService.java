package com.hgnu.diningexpensemanagementsystem.service;

import com.hgnu.diningexpensemanagementsystem.entity.AdminDEMS;

public interface AdminService {
    AdminDEMS login(String adminId, String password);
    AdminDEMS getAdminById(String adminId);
    void updatePassword(String adminId, String password);
}
