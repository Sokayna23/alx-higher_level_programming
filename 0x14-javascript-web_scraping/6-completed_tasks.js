#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, { json: true }, (error, response, todos) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error('Error: Received status code:', response && response.statusCode);
  } else {
    const completedTasksByUser = {};

    // Filter completed tasks and count by user id
    todos.forEach((todo) => {
      if (todo.completed) {
        completedTasksByUser[todo.userId] = (completedTasksByUser[todo.userId] || 0) + 1;
      }
    });

    // Print users with completed tasks as a JavaScript object
    console.log(completedTasksByUser);
  }
});
