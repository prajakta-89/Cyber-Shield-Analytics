CREATE DATABASE cyber_security_db;
USE cyber_security_db;

CREATE TABLE ThreatLogs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    source_ip VARCHAR(50),
    event_type VARCHAR(50), -- e.g., 'DDoS', 'SQL Injection', 'Brute Force'
    severity_level INT,     -- 1 (Low) to 5 (Critical)
    asset_criticality INT,  -- 1 (Laptop) to 10 (Main Database)
    description TEXT
);

-- Adding some dummy data to see results immediately
INSERT INTO ThreatLogs (source_ip, event_type, severity_level, asset_criticality, description)
VALUES 
('192.168.1.105', 'Brute Force', 4, 8, 'Multiple failed SSH attempts'),
('10.0.0.50', 'SQL Injection', 5, 9, 'Attempted UNION SELECT on login form'),
('172.16.254.1', 'Port Scan', 2, 3, 'Nmap scan detected on peripheral subnet');

select * from Threatlogs;