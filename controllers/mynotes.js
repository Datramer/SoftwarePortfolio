const mongodb = require('../db/connect');
const ObjectId =require('mongodb').ObjectId;
const getAll = async (req, res, next) => {
  try{
  const result = await mongodb.getDb().db('MyNotes').collection('Notes').find();
  result.toArray().then((lists) => {
    res.setHeader('Content-Type', 'application/json');
    res.status(200).json(lists);
  });
} catch {
  res.status(200).json('oh no! that didnt work....');
}
  };


const getSingle = async (req, res, next) => {
  try{
  const cardId = new ObjectId(req.params.id);
  const result = await mongodb.getDb().db('MyNotes').collection('Notes').find({ _id: cardId });
  result.toArray().then((lists) => {
    res.setHeader('Content-Type', 'application/json');
    res.status(200).json(lists[0]);
  });
  } catch {
  res.status(200).json('oh no! that didnt work....');
}
  };

  
  const createNote = async (req, res) => {
    try{
    const card = {
      date: req.body.Date,
      note: req.body.Note,
      device: req.body.Device,
      time: req.body.Time,
      
    };
      const response = await mongodb.getDb().db('MyNotes').collection('Notes').insertOne(card);
      if (response .acknowledged) {
      res.status(201).json(response)
      } else {
      res.status(500).json(response.error || 'an error occured during creation of card');
    }
  } catch {
    res.status(200).json('oh no! that didnt work....');
  }
  };


  const changeNote = async (req, res) => {
    try{
    const cardId = new ObjectId(req.params.id);
    const card = {
      date: req.body.Date,
      note: req.body.Note,
      device: req.body.Device,
      time: req.body.Time,
      
    };
      const response = await mongodb.getDb().db('MyNotes').collection('Notes').replaceOne({_id: cardId},card);
      if (response .acknowledged) {
      res.status(204).json(response)
      } else {
      res.status(500).json(response.error || 'an error occured during creation of card');
    }
  } catch {
    res.status(200).json('oh no! that didnt work....');
  }
  };

  const deleteNote = async (req, res) => {
    try{
    const cardId = new ObjectId(req.params.id);
    const response = await mongodb.getDb().db('MyNotes').collection('Notes').deleteOne({ _id: cardId }, true);
    console.log(response);
    if (response.deletedCount > 0) {
      res.status(200).send();
    } else {
      res.status(500).json(response.error || 'error while deleting card')
    }
  } catch {
    res.status(200).json('oh no! that didnt work....');
  }
  };



module.exports = { getAll, getSingle, createNote, changeNote, deleteNote};