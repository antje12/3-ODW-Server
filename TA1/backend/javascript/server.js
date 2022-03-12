const express = require('express');
const mysql = require('mysql2');
const server = express();
server.use(express.urlencoded());

//#region classes
const Person = require('./person');
const dbBroker = require('./dbBroker');
const pool = mysql.createPool({
    host: "database",
    user: "root",
    password: "",
    database: "ta1",
    port: 3306,
    insecureAuth: true,
    waitForConnections: true,
    connectionLimit: 10,
    queueLimit: 0
});
//#endregion

//#region general CORS headers
server.use(function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});
//#endregion

//#region api functions
// curl -X POST -H "Content-Type:application/json" -d "{ \"firstname\": \"John\", \"lastname\": \"Doe\" }" http://localhost:5000/person
server.post('/person', async (req, res) => {

    let body = req.body;
    console.log("/person called - Got input: ", body);

    let firstname = body.firstname;
    let lastname = body.lastname;
    let person = new Person(0, firstname, lastname);

    dbBroker.savePerson(pool, person)
        .then(dbPerson => {
            console.log("/person success");
            let output = JSON.stringify(dbPerson);
            res.send(output);
            return;
        })
        .catch(error => {
            console.log("/person error");
            res.status(400).send(error);
            return;
        });
});

// curl http://localhost:5000/persons
server.get('/persons', async (req, res) => {

    console.log("/persons called");

    dbBroker.listPersons(pool)
        .then(persons => {
            console.log("/persons success");
            let output = JSON.stringify(persons);
            res.send(output);
            return;
        })
        .catch(error => {
            console.log("/persons error");
            res.status(400).send(error);
            return;
        });
});
//#endregion

// general request fallback
server.get('*', (req, res) => {
    res.sendStatus(404)
});
//#endregion

server.listen(5000, () =>
    console.log("Started server at http://localhost:5000!"));
