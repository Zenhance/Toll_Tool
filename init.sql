CREATE TABLE CITIZEN
(
    N_ID               NUMBER,
    NAME                NVARCHAR2(30) NOT NULL ,
    DRIVING_LICENSE_NO NVARCHAR2(25),
    MOBILE_NO          NUMBER NOT NULL,
    CHECK (LENGTH(MOBILE_NO) = 11),
    PRIMARY KEY (N_ID)
);

CREATE TABLE CAR_INFO
(
    REGISTRANT_ID NUMBER,
    REGISTRANT_NAME NVARCHAR2(30),
    PLATE_NO NVARCHAR2(30),
    ENGINE_NO NUMBER,
    CHASSIS_NO NVARCHAR2(30),
    CAR_TYPE NVARCHAR2(20),
    PRIMARY KEY (PLATE_NO),
    FOREIGN KEY (REGISTRANT_ID) REFERENCES CITIZEN(N_ID)
);

CREATE TABLE ACCOUNT
(
    IDENTIFYING_ID NUMBER,
    ACC_NO NUMBER,
    NAME NVARCHAR2(30),
    BALANCE NUMBER,
    PRIMARY KEY (ACC_NO),
    FOREIGN KEY (IDENTIFYING_ID) REFERENCES CITIZEN(N_ID)
);

CREATE TABLE BRIDGE
(
    BRIDGE_ID NVARCHAR2(10),
    TOLL_PLAZA_NO NUMBER,
    PALCE NVARCHAR2(20),
    PRIMARY KEY (BRIDGE_ID)
);

CREATE TABLE TOLL_BOOTH
(
    BOOTH_PLACE NVARCHAR2(10),
    BOOTH_ID NVARCHAR2(20),
    PRIMARY KEY (BOOTH_ID),
    FOREIGN KEY (BOOTH_PLACE) REFERENCES BRIDGE(BRIDGE_ID)
);

CREATE TABLE TOLL
(
    CAR_NO NVARCHAR2(30),
    TOLL_ID NUMBER,
    COLLECTION_BOOTH NVARCHAR2(20),
    TOLL_AMOUNT NUMBER,
    T_DATE DATE,
    PRIMARY KEY (TOLL_ID),
    FOREIGN KEY (CAR_NO) REFERENCES CAR_INFO(PLATE_NO),
    FOREIGN KEY (COLLECTION_BOOTH) REFERENCES  TOLL_BOOTH(BOOTH_ID)
);