db.Students.aggregate([
   {
      $lookup: {
         from: "Exams",
         localField: "examId",    // field in the student collection
         foreignField: "examId",  // field in the exam collection
         as: "examData"
      }
   },
   { $unwind: "$examData"},
   { $set: {"examName": "$examData.name"} },
   { $set: {"description": "$examData.description"} },
   { $set: {"days": "$examData.days"} },
   { $project: { examData: 0} },
])