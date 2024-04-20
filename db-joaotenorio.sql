CREATE DATABASE joaotenorio;
SELECT * FROM joaotenorio.company;
SELECT joaotenorio.GAMES.title, joaotenorio.COMPANY.name FROM joaotenorio.GAMES INNER JOIN joaotenorio.VIDEOGAMES ON joaotenorio.GAMES.id_console = joaotenorio.VIDEOGAMES.id_console INNER JOIN joaotenorio.COMPANY ON joaotenorio.VIDEOGAMES.id_company = joaotenorio.COMPANY.id_company