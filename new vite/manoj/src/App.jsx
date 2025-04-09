import React, { useEffect, useState } from "react";
import axios from "axios";

const baseURL = "http://127.0.0.1:8000/user";

function App() {
  const [users, setUsers] = useState([]);
  const [form, setForm] = useState({
    name: "",
    city: "",
    district: "",
    rollno: ""
  });

  // GET all users
  const fetchUsers = async () => {
    const res = await axios.get(`${baseURL}/getAll`);
    setUsers(res.data);
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  // Handle form input change
  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  // POST - Create user
  const createUser = async () => {
    try {
      await axios.post(`${baseURL}/create`, form);
      fetchUsers();
      setForm({ name: "", city: "", district: "", rollno: "" });
    } catch (err) {
      alert("Error creating user");
    }
  };

  // PUT - Update user
  const updateUser = async () => {
    try {
      await axios.put(`${baseURL}/update`, form);
      fetchUsers();
    } catch (err) {
      alert("Error updating user");
    }
  };

  // DELETE - Delete user
  const deleteUser = async (rollno) => {
    try {
      await axios.delete(`${baseURL}/delete`, { params: { rollno } });
      fetchUsers();
    } catch (err) {
      alert("Error deleting user");
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>User Management</h1>

      <input
        type="text"
        name="rollno"
        placeholder="Roll No"
        value={form.rollno}
        onChange={handleChange}
      />
      <input
        type="text"
        name="name"
        placeholder="Name"
        value={form.name}
        onChange={handleChange}
      />
      <input
        type="text"
        name="city"
        placeholder="City"
        value={form.city}
        onChange={handleChange}
      />
      <input
        type="text"
        name="district"
        placeholder="District"
        value={form.district}
        onChange={handleChange}
      />

      <div style={{ marginTop: "1rem" }}>
        <button onClick={createUser}>Create</button>
        <button onClick={updateUser} style={{ marginLeft: "10px" }}>
          Update
        </button>
      </div>

      <h2 style={{ marginTop: "2rem" }}>User List</h2>
      <ul>
        {users.map((user) => (
          <li key={user.rollno}>
            {user.rollno} - {user.name} - {user.city} - {user.district}
            <button onClick={() => deleteUser(user.rollno)} style={{ marginLeft: "10px" }}>
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
