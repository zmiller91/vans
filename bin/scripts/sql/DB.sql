create database vans;
use vans;

create table listings (
	city varchar(256),
	title varchar(256),
    link varchar(256),
    description blob,
    image varchar(256),
    date datetime,

    primary key (link),
	index `city` (city)
);

create table configuration(
	name varchar(256),
    json blob,
    primary key(name)
);

INSERT INTO configuration
(name, json)
VALUES
('cities', '["denver", "boulder", "omaha", "saltlakecity", "lincoln", "albuquerque", "lasvegas", "phoenix", "desmoines"]'),
('search', '"?query=work+van&format=rss"');
