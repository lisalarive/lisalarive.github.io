import sqlite3

connexion = sqlite3.connect("api_culture.db")
curseur = connexion.cursor()

# table theme
curseur.execute("""
create table if not exists theme(
    idt integer primary key autoincrement, 
    nom varchar(30) not null,
    
    constraint u_nom unique(nom)
);
""")

# table page_wiki
curseur.execute("""
create table if not exists page_wiki(
    idpw integer primary key autoincrement, 
    titre_page varchar(50) not null,  
    idt integer not null, 
    est_traitee integer not null,
    
    constraint u_titre_page unique(titre_page),
    constraint chk_boolean check(est_traitee in (0, 1)),
    constraint fk_theme foreign key(idt) references theme(idt)
);
""")

# table reponse_gem
curseur.execute("""
create table if not exists reponse_gem(
    idrg integer primary key autoincrement, 
    question varchar(200) not null, 
    reponse varchar(100) not null, 
    difficulte varchar(10) not null, 
    idpw integer not null, 
    date_ajout timestamp default current_timestamp not null,
    
    constraint u_question unique(question),
    constraint chk_difficulte check(lower(difficulte) in ('facile', 'moyen', 'difficile')),
    constraint fk_page_wiki foreign key(idpw) references page_wiki(idpw)
);
""")

connexion.commit()
connexion.close()

