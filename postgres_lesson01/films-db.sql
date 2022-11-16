--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5 (Ubuntu 14.5-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.5 (Ubuntu 14.5-0ubuntu0.22.04.1)

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
-- Name: actors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actors (
    id integer NOT NULL,
    name text NOT NULL,
    film_id integer
);


ALTER TABLE public.actors OWNER TO postgres;

--
-- Name: actors_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.actors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actors_id_seq OWNER TO postgres;

--
-- Name: actors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.actors_id_seq OWNED BY public.actors.id;


--
-- Name: directors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.directors (
    id integer NOT NULL,
    name text NOT NULL,
    year text NOT NULL,
    film_id integer NOT NULL
);


ALTER TABLE public.directors OWNER TO postgres;

--
-- Name: directors_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.directors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.directors_id_seq OWNER TO postgres;

--
-- Name: directors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.directors_id_seq OWNED BY public.directors.id;


--
-- Name: film; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.film (
    id integer NOT NULL,
    title text NOT NULL,
    director text NOT NULL,
    year text NOT NULL
);


ALTER TABLE public.film OWNER TO postgres;

--
-- Name: film_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.film_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.film_id_seq OWNER TO postgres;

--
-- Name: film_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.film_id_seq OWNED BY public.film.id;


--
-- Name: actors id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actors ALTER COLUMN id SET DEFAULT nextval('public.actors_id_seq'::regclass);


--
-- Name: directors id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.directors ALTER COLUMN id SET DEFAULT nextval('public.directors_id_seq'::regclass);


--
-- Name: film id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.film ALTER COLUMN id SET DEFAULT nextval('public.film_id_seq'::regclass);


--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actors (id, name, film_id) FROM stdin;
1	Jack Nicholson	6
2	Tom Hanks	11
3	Leonardo DiCaprio	0
4	Gregory Peck	15
5	Marilyn Monroe	2
6	Jodie Foster	9
7	Morgan Freeman	10
8	Harrison Ford	8
9	Gene Kelly	1
10	Anthony Hopkins	9
11	Samuel L. Jackson	16
12	Robin Williams	17
13	Bruce Willis	16
14	Ian McKellen	14
15	Tim Roth	16
16	Uma Thurman	16
17	Mark Hamill	7
18	Sam Neil	12
19	Jeff Goldblum	12
20	Matt Damon	13
21	Vin Diesel	13
\.


--
-- Data for Name: directors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.directors (id, name, year, film_id) FROM stdin;
1	Steven Spielberg	1946-now	8
2	Martin Scorsese	1942-now	0
3	Alfred Hitchcock	1899-1980	3
4	James Cameron	1954-now	0
5	Quentin Tarantino	1963-now	16
6	Christopher Nolan	1970-now	0
7	Stanley Kubrick	1928-1999	4
8	Francis Ford Coppola	1939-now	5
9	David Fincher	1962-now	0
10	David Lynch	1946-now	0
11	Ridley Scott	1937-now	0
12	Wes Anderson	1969-now	0
13	Robert Zemeckis	1952-now	11
14	George Lucas	1944-now	7
15	Gus Van Sant	1952-now	17
16	Robert Mulligan	1925-2008	15
17	Billy Wilder	1906-2002	2
18	Stanley Donen	1924-2019	1
19	Peter Jackson	1961-now	14
20	Milos Forman	1932-2018	6
21	Jonathan Demme	1944-2017	9
22	Frank Darabont	1959-now	10
\.


--
-- Data for Name: film; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.film (id, title, director, year) FROM stdin;
1	Singing in the rain	Stanley Donen	1952
2	Some like it hot	Billy Wilder	1959
3	Psycho	Alfred Hitchcock	1960
4	2001 A space Odyssey	Stanley Kubrick	1968
5	The Godfather	Francis Coppola	1972
6	One flew over the cuckoos nest	Milos Forman	1975
7	Star wars	George Lucas	1977
8	Raiders of the lost ark	Steven Spielberg	1981
9	The Silence of the lambs	Jonathan Demme	1991
10	The Shawshank redemption	Frank Darabont	1994
11	Forrest Gump	Robert Zemeckis	1994
12	Jurassic Park	Steven Spielberg	1993
13	Save private Ryan	Steven Spielberg	1998
14	The Lord of the rings: The Return of the King	Peter Jackson	2003
15	To Kill a Mockingbird	Robert Mulligan	1962
16	Pulp Fiction	Quentin Tarantino	1994
17	Good Will Hunting	Gus Van Sant	1997
\.


--
-- Name: actors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.actors_id_seq', 21, true);


--
-- Name: directors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.directors_id_seq', 22, true);


--
-- Name: film_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.film_id_seq', 17, true);


--
-- Name: actors actors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_pkey PRIMARY KEY (id);


--
-- Name: directors directors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.directors
    ADD CONSTRAINT directors_pkey PRIMARY KEY (id);


--
-- Name: film film_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.film
    ADD CONSTRAINT film_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

