function RoadmapCard({ roadmap }) {
  return (
    <div className="bg-white rounded-3xl shadow-xl p-8">

      <h2 className="text-3xl font-bold mb-6">
        📚 Generated Learning Path
      </h2>

      <div className="whitespace-pre-wrap leading-8 text-gray-700">
        {roadmap}
      </div>

    </div>
  );
}

export default RoadmapCard;