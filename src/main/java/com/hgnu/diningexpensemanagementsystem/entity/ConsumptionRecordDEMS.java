package com.hgnu.diningexpensemanagementsystem.entity;

import lombok.Data;

import java.math.BigDecimal;
import java.time.LocalDateTime;

@Data
public class ConsumptionRecordDEMS {
    private Long recordId;
    private String studentId;
    private String studentName;
    private String staffId;
    private String staffName;
    private BigDecimal amount;
    private LocalDateTime createTime;
}
