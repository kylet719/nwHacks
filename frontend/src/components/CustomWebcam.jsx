import Webcam from "react-webcam";
import { useRef, useState } from "react";

const CustomWebcam = () => {
  const webcamRef = useRef(null);
  const [imgSrc, setImgSrc] = useState(null);

  const capture = async () => {
  
    if (webcamRef.current) {  
      try {
        const imageSrc = webcamRef.current.getScreenshot();
        setImgSrc(imageSrc);

        const response = await fetch('http://127.0.0.1:5000/api/processIMG', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ imageSrc }),
        });
  
        if (response.ok) {
          console.log('Image successfully processed on the backend');

        } else {
          console.error('Failed to process the image on the backend');
        }
      } catch (error) {
        console.error('Error while communicating with the backend', error);
      } 
    }
  };

  const retake = () => {
    setImgSrc(null);
  };

  return (
    <div className="container">
      {imgSrc ? (
        <img src={imgSrc} alt="webcam" />
      ) : (
        <Webcam height={600} width={600} ref={webcamRef} mirrored={true}/>
      )}
      <div className="btn-container">
        {imgSrc ? (
          <button onClick={retake}>Retake photo</button>
        ) : (
          <button onClick={capture}>Capture photo</button>
        )}
      </div>
    </div>
  );
};

export default CustomWebcam;