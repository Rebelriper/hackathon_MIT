const express = require("express");
const fileUpload = require("express-fileupload");
const app = express();

require("dotenv").config();
const PORT = process.env.PORT || 4000;

app.use(express.json());
app.use(
  fileUpload({
    useTempFiles: true,
    tempFileDir: "/tmp/",
  })
);

const cloudinary = require("./Config/cloudinary");
cloudinary.cloudinaryConnect();

app.listen(PORT, () => {
  console.log(`Server is running...`);
});

app.get("/", (req, res) => {
  res.status(200).json({
    success: true,
    status: "Normal",
    message: "Service is Up",
  });
});
