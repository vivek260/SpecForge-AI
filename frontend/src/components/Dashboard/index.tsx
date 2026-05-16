import React from "react";

interface CardData {
  id: number;
  title: string;
  description: string;
  imageSrc: string;
  buttonText: string;
  link: string;
}

export const Dashboard: React.FC = () => {
  const cards: CardData[] = [
    {
      id: 1,
      title: "Code To Spec",
      description:
        "Generate comprehensive functional specifications from source code with AI-powered analysis.",
      imageSrc: "/icons/code_to_spec.png",
      buttonText: "Get Started",
      link: "code-to-spec",
    },
    {
      id: 2,
      title: "Spec To Code",
      description:
        "Generate robust, production-ready source code directly from requirements and technical specs.",
      imageSrc: "/icons/spec_to_code.png",
      buttonText: "Get Started",
      link: "spec-to-code",
    },
  ];

  return (
    <div className="enhanced-cards-container">
      {cards.map((card) => (
        <div key={card.id} className="enhanced-card">
          {/* Top Panel with Gradient Mesh */}
          <div className="enhanced-card-header">
            <div className="icon-wrapper">
              <img
                src={card.imageSrc}
                alt={`${card.title} icon`}
                className="enhanced-card-icon"
              />
            </div>
          </div>

          {/* Bottom Content Area */}
          <div className="enhanced-card-body">
            <h2 className="enhanced-card-title">{card.title}</h2>
            <p className="enhanced-card-description">{card.description}</p>
            <a href={card.link} className="enhanced-btn">
              <span>{card.buttonText}</span>
              <svg
                className="btn-arrow"
                width="16"
                height="16"
                viewBox="0 0 16 16"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M6 12L10 8L6 4"
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                />
              </svg>
            </a>
          </div>
        </div>
      ))}
    </div>
  );
};

export default Dashboard;
