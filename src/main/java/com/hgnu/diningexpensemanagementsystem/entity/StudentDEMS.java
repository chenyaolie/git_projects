package com.hgnu.diningexpensemanagementsystem.entity;

import lombok.Data;

import java.math.BigDecimal;
import java.time.LocalDateTime;

@Data
public class StudentDEMS {
    private String studentId;
    private String studentName;
    private String department;
    private String password;
    private BigDecimal balance;
    private Integer isLost;
    private LocalDateTime createTime;
    private LocalDateTime updateTime;
}
