package com.hgnu.diningexpensemanagementsystem.entity;

import lombok.Data;

import java.time.LocalDateTime;

@Data
public class StaffDEMS {
    private String staffId;
    private String staffName;
    private String password;
    private LocalDateTime createTime;
    private LocalDateTime updateTime;
}
