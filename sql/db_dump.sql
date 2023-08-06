--
-- PostgreSQL database dump
--

-- Dumped from database version 14.8 (Ubuntu 14.8-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.8 (Ubuntu 14.8-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: requests_archive; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.requests_archive (
    id integer NOT NULL,
    angle integer,
    clock integer[],
    request_address character varying(255),
    requested_at timestamp without time zone
);


ALTER TABLE public.requests_archive OWNER TO root;

--
-- Name: requests_archive2; Type: TABLE; Schema: public; Owner: test_user
--

CREATE TABLE public.requests_archive2 (
    id integer NOT NULL,
    angle integer,
    clock integer[],
    requested_at timestamp without time zone,
    request_address character varying(155)
);


ALTER TABLE public.requests_archive2 OWNER TO test_user;

--
-- Name: requests_archive2_id_seq; Type: SEQUENCE; Schema: public; Owner: test_user
--

CREATE SEQUENCE public.requests_archive2_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.requests_archive2_id_seq OWNER TO test_user;

--
-- Name: requests_archive2_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: test_user
--

ALTER SEQUENCE public.requests_archive2_id_seq OWNED BY public.requests_archive2.id;


--
-- Name: requests_archive_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.requests_archive_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.requests_archive_id_seq OWNER TO root;

--
-- Name: requests_archive_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.requests_archive_id_seq OWNED BY public.requests_archive.id;


--
-- Name: requests_archive id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.requests_archive ALTER COLUMN id SET DEFAULT nextval('public.requests_archive_id_seq'::regclass);


--
-- Name: requests_archive2 id; Type: DEFAULT; Schema: public; Owner: test_user
--

ALTER TABLE ONLY public.requests_archive2 ALTER COLUMN id SET DEFAULT nextval('public.requests_archive2_id_seq'::regclass);


--
-- Data for Name: requests_archive; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.requests_archive (id, angle, clock, request_address, requested_at) FROM stdin;
1	30	{1,0}	127.0.0.1	2023-08-03 08:13:52.703736
2	150	{7,0}	127.0.0.1	2023-08-03 08:16:34
3	150	{7,0}	127.0.0.1	2023-08-03 08:16:34
4	168	{11,25}	127.0.0.1	2023-08-03 08:17:41
5	30	{1,0}	127.0.0.1	2023-08-03 08:17:53.194235
19	60	{2,0}	127.0.0.1	2023-08-04 17:00:45
22	60	{2,0}	127.0.0.1	2023-08-04 17:02:34
23	33	{11,54}	127.0.0.1	2023-08-04 17:03:05
24	126	{10,12}	127.0.0.1	2023-08-04 17:05:58
25	126	{10,12}	127.0.0.1	2023-08-04 17:09:39
26	36	{1,12}	127.0.0.1	2023-08-04 17:10:48
27	36	{1,12}	127.0.0.1	2023-08-04 17:12:08
28	36	{1,12}	127.0.0.1	2023-08-04 17:12:49
29	151	{11,22}	127.0.0.1	2023-08-04 17:48:13
30	151	{11,22}	127.0.0.1	2023-08-04 17:50:10
31	151	{11,22}	127.0.0.1	2023-08-04 18:01:10
32	126	{10,12}	127.0.0.1	2023-08-04 20:48:28
33	126	{10,12}	127.0.0.1	2023-08-04 20:48:53
34	143	{10,15}	127.0.0.1	2023-08-04 20:49:13
35	143	{10,15}	127.0.0.1	2023-08-04 20:49:48
36	143	{10,15}	127.0.0.1	2023-08-04 21:09:18
37	143	{10,15}	127.0.0.1	2023-08-04 21:10:43
38	143	{10,15}	127.0.0.1	2023-08-04 21:11:28
39	143	{10,15}	127.0.0.1	2023-08-04 21:11:48
40	143	{10,15}	127.0.0.1	2023-08-04 21:16:39
41	143	{10,15}	127.0.0.1	2023-08-04 21:19:27
42	53	{1,15}	127.0.0.1	2023-08-04 21:20:45
43	53	{1,15}	127.0.0.1	2023-08-04 21:23:44
44	53	{1,15}	127.0.0.1	2023-08-04 21:24:08
45	113	{11,15}	127.0.0.1	2023-08-04 21:24:54
46	113	{11,15}	127.0.0.1	2023-08-04 21:25:39
47	113	{11,15}	127.0.0.1	2023-08-04 21:26:56
48	113	{11,15}	127.0.0.1	2023-08-04 21:26:59
49	113	{11,15}	127.0.0.1	2023-08-04 21:26:59
50	126	{10,12}	127.0.0.1	2023-08-06 13:59:16
51	126	{10,12}	127.0.0.1	2023-08-06 13:59:30
52	126	{10,12}	127.0.0.1	2023-08-06 14:01:28
53	126	{10,12}	127.0.0.1	2023-08-06 14:02:03
54	126	{10,12}	127.0.0.1	2023-08-06 14:15:28
55	24	{3,12}	127.0.0.1	2023-08-06 14:17:35
56	24	{3,12}	127.0.0.1	2023-08-06 14:22:26
57	24	{3,12}	127.0.0.1	2023-08-06 14:30:40
58	24	{3,12}	127.0.0.1	2023-08-06 14:59:38
59	90	{3,0}	127.0.0.1	2023-08-06 14:59:59
60	106	{4,41}	127.0.0.1	2023-08-06 15:16:08
61	100	{4,40}	127.0.0.1	2023-08-06 15:16:51
62	15	{6,30}	127.0.0.1	2023-08-06 15:44:01
63	90	{3,0}	127.0.0.1	2023-08-06 15:44:01
64	15	{6,30}	127.0.0.1	2023-08-06 15:44:28
65	90	{3,0}	127.0.0.1	2023-08-06 15:44:28
66	15	{6,30}	127.0.0.1	2023-08-06 15:46:28
67	90	{3,0}	127.0.0.1	2023-08-06 15:46:28
68	15	{6,30}	127.0.0.1	2023-08-06 15:49:46
69	90	{3,0}	127.0.0.1	2023-08-06 15:49:46
70	15	{6,30}	127.0.0.1	2023-08-06 15:50:09
71	90	{3,0}	127.0.0.1	2023-08-06 15:50:09
72	15	{6,30}	127.0.0.1	2023-08-06 15:50:34
73	90	{3,0}	127.0.0.1	2023-08-06 15:50:34
74	15	{6,30}	127.0.0.1	2023-08-06 15:50:39
75	90	{3,0}	127.0.0.1	2023-08-06 15:50:39
76	15	{6,30}	127.0.0.1	2023-08-06 15:51:04
77	90	{3,0}	127.0.0.1	2023-08-06 15:51:04
78	15	{6,30}	127.0.0.1	2023-08-06 15:51:09
79	90	{3,0}	127.0.0.1	2023-08-06 15:51:09
80	15	{6,30}	127.0.0.1	2023-08-06 15:53:31
81	90	{3,0}	127.0.0.1	2023-08-06 15:53:31
\.


--
-- Data for Name: requests_archive2; Type: TABLE DATA; Schema: public; Owner: test_user
--

COPY public.requests_archive2 (id, angle, clock, requested_at, request_address) FROM stdin;
\.


--
-- Name: requests_archive2_id_seq; Type: SEQUENCE SET; Schema: public; Owner: test_user
--

SELECT pg_catalog.setval('public.requests_archive2_id_seq', 1, false);


--
-- Name: requests_archive_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.requests_archive_id_seq', 81, true);


--
-- Name: requests_archive2 requests_archive2_pkey; Type: CONSTRAINT; Schema: public; Owner: test_user
--

ALTER TABLE ONLY public.requests_archive2
    ADD CONSTRAINT requests_archive2_pkey PRIMARY KEY (id);


--
-- Name: requests_archive requests_archive_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.requests_archive
    ADD CONSTRAINT requests_archive_pkey PRIMARY KEY (id);


--
-- Name: TABLE requests_archive; Type: ACL; Schema: public; Owner: root
--

GRANT ALL ON TABLE public.requests_archive TO test_user;


--
-- PostgreSQL database dump complete
--

