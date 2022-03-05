//
//  ContentView.swift
//  RockPaperScissors
//
//  Created by Jakub Dąbrowski on 27/02/2022.
//

import SwiftUI

struct ContentView: View {
    
    static let rps = ["Rock", "Paper", "Scissors"]
    
    @State private var userChoice = ""
    @State private var appChoice = (rps.shuffled())[0]
    @State private var winner = ""
    
    @State private var showingScore = false
    
    @State private var trialCounter = 1
    @State private var showingResults = false
    
    @State private var scoreTitle = ""
    @State private var score = 0
    
    
    
    var body: some View {
        ZStack{
            LinearGradient(stops: [
                .init(color: Color(red: 0.75, green: 0.15, blue: 0.26), location: 0.3),
                .init(color: Color(red: 0.0, green: 0.0, blue: 0.0), location: 1)
            ],
        startPoint: .top, endPoint: .bottom)
                           
            
            VStack{
                
                Spacer()
                
                Text("""
                    Rock! Paper!
                    Scissors!
                    """)
                    .font(.largeTitle.bold())
                    .multilineTextAlignment(.center)
                    .padding()
                VStack{
                    Text("Choose your answer")
                        .padding()
                    
                    HStack {
                        Button("👊") {
                            userChoice = "Rock"
                            determineWinner()
                        }
                        Button("✋") {
                            userChoice = "Paper"
                            determineWinner()
                        }
                        Button("✌️") {
                            userChoice = "Scissors"
                            determineWinner()
                        }
                    }
                }
                .padding(.vertical, 20)
                .background(.thinMaterial)
                .clipShape(RoundedRectangle(cornerRadius: 20))
                
                Spacer()
                Spacer()
            }
            .alert(scoreTitle, isPresented: $showingScore) {
                Button("Continue", action: nextTrial) }
            message : {
                Text("""
                        Your enemy chose \(appChoice).
                        Your score is \(score)
                    """)
            }
            .alert("Game over", isPresented: $showingResults) {
                Button("Start again", action: newGame)
            } message : {
                Text("Your final score was \(score)")
            }
            
        }
    }
    
    func nextTrial() {
        trialCounter += 1
        appChoice = (ContentView.rps.shuffled())[0]
    }
    
    func newGame() {
        trialCounter = 0
        score = 0
        nextTrial()
    }

    func determineWinner() {
        
        if userChoice == appChoice {
            scoreTitle = "It's a draw"
        }
            
        else if userChoice == "Rock" && appChoice == "Paper" {
            scoreTitle = "You lose"
            if score > 0 {
            score -= 1
            }
        }

        
        else if userChoice == "Rock" && appChoice == "Scissors" {
            scoreTitle = "You win"
            score += 1
            }
        
        else if userChoice == "Scissors" && appChoice == "Rock" {
            scoreTitle = "You lose"
            if score > 0 {
            score -= 1
            }
            }
        
        else if userChoice == "Scissors" && appChoice == "Paper" {
            scoreTitle = "You win"
            score += 1
            }
            
        else if userChoice == "Paper" && appChoice == "Scissors" {
            scoreTitle = "You lose"
            if score > 0 {
            score -= 1
            }
        }
            
        else if userChoice == "Paper" && appChoice == "Rock" {
            scoreTitle = "You win"
            score += 1
            }
        
        if trialCounter == 7 {
            showingResults = true
            
        }else{
        
        showingScore = true
        }
    }
    }
    


struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
