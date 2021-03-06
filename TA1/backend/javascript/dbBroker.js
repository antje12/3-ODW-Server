const mysql = require('mysql2');
const Person = require('./person');

module.exports = {
  savePerson: function (pool, person) {

    return new Promise(function (resolve, reject) {
      pool.getConnection(async function (err, connection) {
        if (err) {
          console.log(er);
          reject(err);
        }

        let dbPerson = await dbCall(connection,
          "INSERT INTO Person (Firstname, Lastname) VALUES (?, ?)",
          [person.Firstname, person.Lastname]);
        let personID = dbPerson.insertId;;
        person.PersonID = personID;

        pool.releaseConnection(connection);
        resolve(person);
        return;
      });
    });
  },
  listPersons: function (pool) {

    return new Promise(function (resolve, reject) {
      pool.getConnection(async function (err, connection) {
        if (err) {
          console.log(er);
          reject(err);
        }

        let dbPersons = await dbCall(connection,
          "SELECT * FROM Person",
          []);

        let result = [];
        dbPersons.forEach(dbPerson => {
          let person = new Person(
            dbPerson.PersonID,
            dbPerson.Firstname,
            dbPerson.Lastname);
          result.push(person);
        });

        pool.releaseConnection(connection);
        resolve(result);
        return;
      });
    });
  }
};

async function dbCall(connection, sql, args) {

  let res;
  await connection.promise()
    .query(sql, args)
    .then(([result]) => {
      res = result;
    })
    .catch(er => {
      console.log(er);
      throw new Error("DB error: ", err)
    });
  return res;
}
