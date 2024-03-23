// script.js

const url = 'http://localhost:8000/api/contacts/'

window.getContacts = async function (skip = 0, limit = 100) {
  const response = await fetch(`${url}?skip=${skip}&limit=${limit}`)
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`)
  }
  const contacts = await response.json()
  return contacts
}

window.createContact = async function (contact) {
  const response = await fetch(`${url}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(contact),
  })
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`)
  }
}

window.editContact = async function (contact) {
  const response = await fetch(`${url}${contact.id}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(contact),
  })
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`)
  }
}

window.deleteContact = async function (id) {
  const response = await fetch(`${url}${id}`, {
    method: 'DELETE',
  })
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`)
  }
}

window.getBirthdays = async function (contacts) {
  try {
    const response = await fetch('http://localhost:8000/api/contacts/birthdays/');
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const birthdays = await response.json();
    contacts.splice(0, contacts.length, ...birthdays); // Оновити стан contacts
  } catch (error) {
    console.error('Error fetching birthdays:', error.message || error);
  }
}

window.searchContacts = async function () {
  const firstName = document.getElementById('searchFirstName').value;
  const lastName = document.getElementById('searchLastName').value;
  const email = document.getElementById('searchEmail').value;

  this.searchResults = [];

  const response = await fetch(`${url}/search?first_name=${firstName}&last_name=${lastName}&email=${email}`, {
    method: 'GET', // Use GET method for searching
    headers: {
      'accept': 'application/json',
    },
  });

  if (!response.ok) {
    throw new Error(`Error fetching contacts: ${response.statusText}`);
  }

  const data = await response.json();
  this.searchResults = data;
}
