const express = require('express');
const {auth, requiresAuth} = require('express-openid-connect');
const proNotes = require('../controllers/mynotes');


const router = express.Router();
router.get('/', proNotes.getAll);
router.get('/:id',requiresAuth(), proNotes.getSingle);
router.post('/', proNotes.createNote);
router.put('/:id',proNotes.changeNote);
router.delete('/:id',proNotes.deleteNote);

module.exports = router;
