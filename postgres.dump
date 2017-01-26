--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.5
-- Dumped by pg_dump version 9.5.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: class; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE class (
    classnumber character varying(15) NOT NULL,
    facid character varying(15),
    schedule character varying(15),
    room character varying(15)
);


ALTER TABLE class OWNER TO postgres;

--
-- Name: enroll; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE enroll (
    stuid character varying(15) NOT NULL,
    classnumber character varying(15) NOT NULL,
    grade character varying(5)
);


ALTER TABLE enroll OWNER TO postgres;

--
-- Name: faculty; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE faculty (
    facid character varying(15) NOT NULL,
    name character varying(15),
    department character varying(15),
    rank character varying(15)
);


ALTER TABLE faculty OWNER TO postgres;

--
-- Name: student; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE student (
    stuid character varying(15) NOT NULL,
    lastname character varying(15),
    firstname character varying(15),
    major character varying(15),
    credits integer
);


ALTER TABLE student OWNER TO postgres;

--
-- Data for Name: class; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY class (classnumber, facid, schedule, room) FROM stdin;
ART103A	F101	MWF9	H221
CSC201A	F105	TuThF10	M110
CSC203A	F105	MThF12	M110
HST205A	F115	MWF11	H221
MTH101B	F110	MTuTh9	H225
MTH103C	F110	MWF11	H225
\.


--
-- Data for Name: enroll; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY enroll (stuid, classnumber, grade) FROM stdin;
S1001	ART103A	A
S1001	HST205A	C
S1002	ART103A	D
S1002	CSC201A	F
S1002	MTH103C	B
S1010	ART103A	
S1010	MTH103C	
S1020	CSC201A	B
S1020	MTH101B	A
\.


--
-- Data for Name: faculty; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY faculty (facid, name, department, rank) FROM stdin;
F101	Adams	Art	Professor
F105	Tanaka	CSC	Instructor
F110	Byrne	Math	Assistant
F115	Smith	History	Associate
F221	Smith	CSC	Professor
\.


--
-- Data for Name: student; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY student (stuid, lastname, firstname, major, credits) FROM stdin;
S1001	Smith	Tom	History	90
S1002	Chin	Ann	Math	36
S1005	Lee	Perry	History	3
S1010	Burns	Edward	Art	63
S1013	McCarthy	Owen	Math	0
S1015	Jones	Mary	Math	42
S1020	Rivera	Jane	CSC	15
\.


--
-- Name: class_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY class
    ADD CONSTRAINT class_pkey PRIMARY KEY (classnumber);


--
-- Name: enroll_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY enroll
    ADD CONSTRAINT enroll_pkey PRIMARY KEY (stuid, classnumber);


--
-- Name: faculty_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY faculty
    ADD CONSTRAINT faculty_pkey PRIMARY KEY (facid);


--
-- Name: student_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY student
    ADD CONSTRAINT student_pkey PRIMARY KEY (stuid);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- Name: class; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE class FROM PUBLIC;
REVOKE ALL ON TABLE class FROM postgres;
GRANT ALL ON TABLE class TO postgres;
GRANT ALL ON TABLE class TO testuser;


--
-- Name: enroll; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE enroll FROM PUBLIC;
REVOKE ALL ON TABLE enroll FROM postgres;
GRANT ALL ON TABLE enroll TO postgres;
GRANT ALL ON TABLE enroll TO testuser;


--
-- Name: faculty; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE faculty FROM PUBLIC;
REVOKE ALL ON TABLE faculty FROM postgres;
GRANT ALL ON TABLE faculty TO postgres;
GRANT ALL ON TABLE faculty TO testuser;


--
-- Name: student; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE student FROM PUBLIC;
REVOKE ALL ON TABLE student FROM postgres;
GRANT ALL ON TABLE student TO postgres;
GRANT ALL ON TABLE student TO testuser;


--
-- PostgreSQL database dump complete
--

