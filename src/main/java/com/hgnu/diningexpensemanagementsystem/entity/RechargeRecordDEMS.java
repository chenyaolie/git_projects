package com.hgnu.diningexpensemanagementsystem.entity;

import lombok.Data;

import java.math.BigDecimal;
import java.time.LocalDateTime;

@Data
public class RechargeRecordDEMS {
    private Long recordId;
    private String studentId;
    private String studentName;
    private BigDecimal amount;
    private Integer type;
    private String operatorId;
    private String operatorName;
    private LocalDateTime createTime;
}
