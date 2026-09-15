package com.hgnu.diningexpensemanagementsystem.entity;

import lombok.Data;

import java.math.BigDecimal;
import java.time.LocalDateTime;

@Data
public class RechargeApplicationDEMS {
    private Long applicationId;
    private String studentId;
    private String studentName;
    private BigDecimal amount;
    private Integer status;
    private String adminId;
    private String adminName;
    private LocalDateTime applyTime;
    private LocalDateTime auditTime;
}
