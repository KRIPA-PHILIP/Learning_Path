import { useState } from "react";
import api from "../services/api";

import Navbar from "../components/Navbar";
import GoalForm from "../components/GoalForm";
import LoadingSpinner from "../components/LoadingSpinner";
import RoadmapCard from "../components/RoadmapCard";

function Home() {
  const [goal, setGoal] = useState("");
  const [loading, setLoading] = useState(false);
  const [learningPath, setLearningPath] = useState("");
  const [error, setError] = useState("");

  const generateLearningPath = async () => {
    if (!goal.trim()) {
      setError("Please enter a career goal.");
      return;
    }

    setLoading(true);
    setError("");

    try {
      const response = await api.post("/generate-learning-path", {
        goal,
      });

      setLearningPath(response.data.learning_path);
    } catch (err) {
      console.error(err);
      setError("Unable to generate learning path.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">

      {loading && <LoadingSpinner />}

      <Navbar />

      <section className="max-w-6xl mx-auto px-6 py-16">

        <div className="text-center">

          <h1 className="text-6xl font-black">
            Build your
            <span className="gradient-text"> Learning Path</span>
          </h1>

          <p className="mt-6 text-xl text-gray-600">
            AI Powered Career Roadmaps
          </p>

        </div>

        <GoalForm
          goal={goal}
          setGoal={setGoal}
          generateLearningPath={generateLearningPath}
        />

        {error && (
          <div className="mt-6 bg-red-100 text-red-600 p-4 rounded-xl">
            {error}
          </div>
        )}

      </section>

      {learningPath && (
        <section
          id="results"
          className="max-w-6xl mx-auto px-6 pb-20"
        >
          <RoadmapCard roadmap={learningPath} />
        </section>
      )}

    </div>
  );
}

export default Home;