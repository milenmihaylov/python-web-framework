--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2 (Ubuntu 15.2-1.pgdg20.04+1)
-- Dumped by pg_dump version 15.2 (Ubuntu 15.2-1.pgdg20.04+1)

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
-- Name: cat; Type: TABLE; Schema: public; Owner: db_admin
--

CREATE TABLE public.cat (
    cat_id bigint NOT NULL,
    cat_name character varying(15) NOT NULL,
    cat_age integer NOT NULL,
    owner_id integer NOT NULL
);


ALTER TABLE public.cat OWNER TO db_admin;

--
-- Name: cat_cat_id_seq; Type: SEQUENCE; Schema: public; Owner: db_admin
--

CREATE SEQUENCE public.cat_cat_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cat_cat_id_seq OWNER TO db_admin;

--
-- Name: cat_cat_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: db_admin
--

ALTER SEQUENCE public.cat_cat_id_seq OWNED BY public.cat.cat_id;


--
-- Name: cat_room_cat_room_id_seq; Type: SEQUENCE; Schema: public; Owner: db_admin
--

CREATE SEQUENCE public.cat_room_cat_room_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cat_room_cat_room_id_seq OWNER TO db_admin;

--
-- Name: cat_room; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cat_room (
    cat_room_id bigint DEFAULT nextval('public.cat_room_cat_room_id_seq'::regclass) NOT NULL,
    register_date date NOT NULL,
    unregister_date date NOT NULL,
    hotel_id bigint NOT NULL,
    cat_id bigint NOT NULL
);


ALTER TABLE public.cat_room OWNER TO postgres;

--
-- Name: dog; Type: TABLE; Schema: public; Owner: db_admin
--

CREATE TABLE public.dog (
    dog_id bigint NOT NULL,
    dog_name character varying(20) NOT NULL,
    dog_age integer NOT NULL,
    owner_id integer NOT NULL
);


ALTER TABLE public.dog OWNER TO db_admin;

--
-- Name: dog_dog_id_seq; Type: SEQUENCE; Schema: public; Owner: db_admin
--

CREATE SEQUENCE public.dog_dog_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dog_dog_id_seq OWNER TO db_admin;

--
-- Name: dog_dog_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: db_admin
--

ALTER SEQUENCE public.dog_dog_id_seq OWNED BY public.dog.dog_id;


--
-- Name: dog_room; Type: TABLE; Schema: public; Owner: db_admin
--

CREATE TABLE public.dog_room (
    dog_room_id bigint NOT NULL,
    register_date date NOT NULL,
    unregister_date date NOT NULL,
    hotel_id integer NOT NULL,
    dog_id integer NOT NULL
);


ALTER TABLE public.dog_room OWNER TO db_admin;

--
-- Name: dog_room_dog_room_id_seq; Type: SEQUENCE; Schema: public; Owner: db_admin
--

CREATE SEQUENCE public.dog_room_dog_room_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dog_room_dog_room_id_seq OWNER TO db_admin;

--
-- Name: dog_room_dog_room_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: db_admin
--

ALTER SEQUENCE public.dog_room_dog_room_id_seq OWNED BY public.dog_room.dog_room_id;


--
-- Name: hotel; Type: TABLE; Schema: public; Owner: db_admin
--

CREATE TABLE public.hotel (
    hotel_id bigint NOT NULL,
    hotel_name character varying(25) NOT NULL,
    hotel_stars integer NOT NULL
);


ALTER TABLE public.hotel OWNER TO db_admin;

--
-- Name: hotel_hotel_id_seq; Type: SEQUENCE; Schema: public; Owner: db_admin
--

CREATE SEQUENCE public.hotel_hotel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hotel_hotel_id_seq OWNER TO db_admin;

--
-- Name: hotel_hotel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: db_admin
--

ALTER SEQUENCE public.hotel_hotel_id_seq OWNED BY public.hotel.hotel_id;


--
-- Name: owner; Type: TABLE; Schema: public; Owner: db_admin
--

CREATE TABLE public.owner (
    owner_id bigint NOT NULL,
    owner_name character varying(15) NOT NULL,
    owner_age integer NOT NULL
);


ALTER TABLE public.owner OWNER TO db_admin;

--
-- Name: owner_owner_id_seq; Type: SEQUENCE; Schema: public; Owner: db_admin
--

CREATE SEQUENCE public.owner_owner_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.owner_owner_id_seq OWNER TO db_admin;

--
-- Name: owner_owner_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: db_admin
--

ALTER SEQUENCE public.owner_owner_id_seq OWNED BY public.owner.owner_id;


--
-- Name: cat cat_id; Type: DEFAULT; Schema: public; Owner: db_admin
--

ALTER TABLE ONLY public.cat ALTER COLUMN cat_id SET DEFAULT nextval('public.cat_cat_id_seq'::regclass);


--
-- Name: dog dog_id; Type: DEFAULT; Schema: public; Owner: db_admin
--

ALTER TABLE ONLY public.dog ALTER COLUMN dog_id SET DEFAULT nextval('public.dog_dog_id_seq'::regclass);


--
-- Name: dog_room dog_room_id; Type: DEFAULT; Schema: public; Owner: db_admin
--

ALTER TABLE ONLY public.dog_room ALTER COLUMN dog_room_id SET DEFAULT nextval('public.dog_room_dog_room_id_seq'::regclass);


--
-- Name: hotel hotel_id; Type: DEFAULT; Schema: public; Owner: db_admin
--

ALTER TABLE ONLY public.hotel ALTER COLUMN hotel_id SET DEFAULT nextval('public.hotel_hotel_id_seq'::regclass);


--
-- Name: owner owner_id; Type: DEFAULT; Schema: public; Owner: db_admin
--

ALTER TABLE ONLY public.owner ALTER COLUMN owner_id SET DEFAULT nextval('public.owner_owner_id_seq'::regclass);


--
-- Data for Name: cat; Type: TABLE DATA; Schema: public; Owner: db_admin
--

COPY public.cat (cat_id, cat_name, cat_age, owner_id) FROM stdin;
2	Jessy	7	3
3	Bubbles	3	2
\.


--
-- Data for Name: cat_room; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cat_room (cat_room_id, register_date, unregister_date, hotel_id, cat_id) FROM stdin;
1	2020-09-09	2020-10-10	2	2
5	2020-06-20	2020-06-23	2	3
\.


--
-- Data for Name: dog; Type: TABLE DATA; Schema: public; Owner: db_admin
--

COPY public.dog (dog_id, dog_name, dog_age, owner_id) FROM stdin;
2	Bully	3	3
3	Rousey	5	1
\.


--
-- Data for Name: dog_room; Type: TABLE DATA; Schema: public; Owner: db_admin
--

COPY public.dog_room (dog_room_id, register_date, unregister_date, hotel_id, dog_id) FROM stdin;
1	2020-06-08	2020-06-10	1	1
2	2020-06-10	2020-06-15	2	2
3	2020-06-20	2020-06-23	2	3
\.


--
-- Data for Name: hotel; Type: TABLE DATA; Schema: public; Owner: db_admin
--

COPY public.hotel (hotel_id, hotel_name, hotel_stars) FROM stdin;
1	Grand Pets Hotel	5
2	Pets Heaven	2
\.


--
-- Data for Name: owner; Type: TABLE DATA; Schema: public; Owner: db_admin
--

COPY public.owner (owner_id, owner_name, owner_age) FROM stdin;
1	Peter	26
2	George	32
3	Amy	67
\.


--
-- Name: cat_cat_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_admin
--

SELECT pg_catalog.setval('public.cat_cat_id_seq', 3, true);


--
-- Name: cat_room_cat_room_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_admin
--

SELECT pg_catalog.setval('public.cat_room_cat_room_id_seq', 6, true);


--
-- Name: dog_dog_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_admin
--

SELECT pg_catalog.setval('public.dog_dog_id_seq', 3, true);


--
-- Name: dog_room_dog_room_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_admin
--

SELECT pg_catalog.setval('public.dog_room_dog_room_id_seq', 3, true);


--
-- Name: hotel_hotel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_admin
--

SELECT pg_catalog.setval('public.hotel_hotel_id_seq', 2, true);


--
-- Name: owner_owner_id_seq; Type: SEQUENCE SET; Schema: public; Owner: db_admin
--

SELECT pg_catalog.setval('public.owner_owner_id_seq', 3, true);


--
-- Name: cat cat_pkey; Type: CONSTRAINT; Schema: public; Owner: db_admin
--

ALTER TABLE ONLY public.cat
    ADD CONSTRAINT cat_pkey PRIMARY KEY (cat_id);


--
-- Name: cat_room cat_room_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cat_room
    ADD CONSTRAINT cat_room_pkey PRIMARY KEY (cat_room_id);


--
-- Name: dog dog_pkey; Type: CONSTRAINT; Schema: public; Owner: db_admin
--

ALTER TABLE ONLY public.dog
    ADD CONSTRAINT dog_pkey PRIMARY KEY (dog_id);


--
-- Name: dog_room dog_room_pkey; Type: CONSTRAINT; Schema: public; Owner: db_admin
--

ALTER TABLE ONLY public.dog_room
    ADD CONSTRAINT dog_room_pkey PRIMARY KEY (dog_room_id);


--
-- Name: hotel hotel_pkey; Type: CONSTRAINT; Schema: public; Owner: db_admin
--

ALTER TABLE ONLY public.hotel
    ADD CONSTRAINT hotel_pkey PRIMARY KEY (hotel_id);


--
-- Name: owner owner_pkey; Type: CONSTRAINT; Schema: public; Owner: db_admin
--

ALTER TABLE ONLY public.owner
    ADD CONSTRAINT owner_pkey PRIMARY KEY (owner_id);


--
-- Name: cat cat_owner_owner_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: db_admin
--

ALTER TABLE ONLY public.cat
    ADD CONSTRAINT cat_owner_owner_id_fk FOREIGN KEY (owner_id) REFERENCES public.owner(owner_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: cat_room cat_room_cat_cat_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cat_room
    ADD CONSTRAINT cat_room_cat_cat_id_fk FOREIGN KEY (cat_id) REFERENCES public.cat(cat_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: dog dog_owner_owner_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: db_admin
--

ALTER TABLE ONLY public.dog
    ADD CONSTRAINT dog_owner_owner_id_fk FOREIGN KEY (owner_id) REFERENCES public.owner(owner_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: dog_room dog_room_hotel_hotel_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: db_admin
--

ALTER TABLE ONLY public.dog_room
    ADD CONSTRAINT dog_room_hotel_hotel_id_fk FOREIGN KEY (hotel_id) REFERENCES public.hotel(hotel_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: cat_room hotel_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cat_room
    ADD CONSTRAINT hotel_id FOREIGN KEY (hotel_id) REFERENCES public.hotel(hotel_id);


--
-- PostgreSQL database dump complete
--

