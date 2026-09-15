package com.hgnu.diningexpensemanagementsystem;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.ApplicationRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import java.awt.Desktop;
import java.net.URI;

@SpringBootApplication
@MapperScan("com.hgnu.diningexpensemanagementsystem.mapper")
public class DiningExpenseManagementSystemApplication {

    public static void main(String[] args) {
        SpringApplication.run(DiningExpenseManagementSystemApplication.class, args);
    }

    @Bean
    public ApplicationRunner openBrowser() {
        return args -> {
            try {
                String url = "http://localhost:8080";
                Desktop.getDesktop().browse(new URI(url));
                System.out.println("浏览器已自动打开: " + url);
            } catch (Exception e) {
                System.out.println("无法自动打开浏览器，请手动访问 http://localhost:8080");
            }
        };
    }

}
