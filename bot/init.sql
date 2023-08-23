--
-- PostgreSQL database dump
--

-- Dumped from database version 13.3
-- Dumped by pg_dump version 13.3

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
-- Name: current_week; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.current_week (
    id integer NOT NULL,
    prediction character varying(255),
    user_id integer,
    results character varying(255),
    created_at timestamp without time zone
);


ALTER TABLE public.current_week OWNER TO postgres;

--
-- Name: current_week_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.current_week_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.current_week_id_seq OWNER TO postgres;

--
-- Name: current_week_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.current_week_id_seq OWNED BY public.current_week.id;


--
-- Name: season; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.season (
    id integer NOT NULL,
    week integer,
    user_id integer,
    points integer,
    created_at timestamp without time zone
);


ALTER TABLE public.season OWNER TO postgres;

--
-- Name: season_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.season_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.season_id_seq OWNER TO postgres;

--
-- Name: season_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.season_id_seq OWNED BY public.season.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(255),
    secret character varying(255),
    created_at timestamp without time zone
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: current_week id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.current_week ALTER COLUMN id SET DEFAULT nextval('public.current_week_id_seq'::regclass);


--
-- Name: season id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.season ALTER COLUMN id SET DEFAULT nextval('public.season_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: current_week; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.current_week (id, prediction, user_id, results, created_at) FROM stdin;
1	11 21 11 32 21 10 01 20 01 02	4	\N	\N
2	22 11 12 32 31 12 12 20 12 22	2	\N	\N
3	11 10 21 00 31 21 02 30 12 11	6	\N	\N
4	21 11 12 31 20 21 20 20 12 13	3	\N	\N
5	12 11 12 20 31 22 02 20 01 13	5	\N	\N
\.


--
-- Data for Name: season; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.season (id, week, user_id, points, created_at) FROM stdin;
1	1	5	9	\N
2	1	6	7	\N
3	1	3	14	\N
4	1	2	13	\N
5	1	4	8	\N
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, username, secret, created_at) FROM stdin;
2	Max1mKu	ОУСБГ	\N
3	Чебурашка	хочудойки	\N
4	kolyandos	password	\N
5	ААА	ЖС	\N
6	TiT11rus	megdubulok	\N
\.


--
-- Name: current_week_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.current_week_id_seq', 5, true);


--
-- Name: season_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.season_id_seq', 5, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 6, true);


--
-- Name: current_week current_week_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.current_week
    ADD CONSTRAINT current_week_pkey PRIMARY KEY (id);


--
-- Name: season season_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.season
    ADD CONSTRAINT season_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: season fk_users_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.season
    ADD CONSTRAINT fk_users_id FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: current_week fk_users_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.current_week
    ADD CONSTRAINT fk_users_id FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

