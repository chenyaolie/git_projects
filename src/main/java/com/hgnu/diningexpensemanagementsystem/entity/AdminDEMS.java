package com.hgnu.diningexpensemanagementsystem.entity;

import lombok.Data;

import java.time.LocalDateTime;

@Data
public class AdminDEMS {
    private String adminId;
    private String adminName;
    private String password;
    private LocalDateTime createTime;
    private LocalDateTime updateTime;
}
