import { useState } from "react";

export default function Home() {
  const [resume, setResume] = useState("");
  const [jobDescription, setJobDescription] = useState("");
  const [result, setResult] = useState("");

  const generateResume = async () => {
    const response = await fetch(
      "http://localhost:8000/generate/",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          resume,
          job_description: jobDescription,
        }),
      }
    );

    const data = await response.json();

    setResult(data.generated_resume);
  };

  return (
    <div style={{ padding: "30px" }}>
      <h1>AI Job Assistant</h1>

      <h3>Master Resume</h3>

      <textarea
        rows="10"
        cols="100"
        value={resume}
        onChange={(e) => setResume(e.target.value)}
      />

      <h3>Job Description</h3>

      <textarea
        rows="10"
        cols="100"
        value={jobDescription}
        onChange={(e) =>
          setJobDescription(e.target.value)
        }
      />

      <br />
      <br />

      <button onClick={generateResume}>
        Generate ATS Resume
      </button>

      <hr />

      <h3>Generated Resume</h3>

      <pre>{result}</pre>
    </div>
  );
}
