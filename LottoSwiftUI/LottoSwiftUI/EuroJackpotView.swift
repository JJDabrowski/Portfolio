//
//  EuroJackpotView.swift
//  LottoSwiftUI
//
//  Created by Jakub Dąbrowski on 05/01/2022.
//

import SwiftUI
import Combine


private final class EuroJackpotViewState: ObservableObject {

@Published var euroJackpotResultMain = ""
@Published var euroJackpotResultSecondary = ""
    
}

struct EuroJackpotView: View {
    
    @Environment(\.presentationMode) var presentationMode: Binding<PresentationMode>
    
    @StateObject private var state = EuroJackpotViewState()
    
    func allTogether(_ SetEuroJackPot:Set<Int>, _ Scope:ClosedRange<Int>) -> (Set<Int>){

        func iterateAndRemove3() -> (Set<Int>, Set<Int>){
        
            var numbers = SetEuroJackPot
            let scope = Scope
        
            var results = Set<Int>()
        
            for _ in scope{
                let randomNumbers = numbers.randomElement()!
                results.insert(randomNumbers)
                numbers.remove(randomNumbers)
            }
        
            return (numbers, results)
        }

        let runFunction = iterateAndRemove3()
        let functionResult = runFunction.1

        return (functionResult)
    }
    
    var buttonBack : some View { Button(action: {
            self.presentationMode.wrappedValue.dismiss()
            }) {
                    Text("< Powrót")
            }
        }
    
    
    var body: some View {
        VStack(spacing: 20){
            Text("Euro Jackpot \n Chybił-trafił")
                .font(.headline)
                .foregroundColor(.yellow)
                .multilineTextAlignment(.center)
                .padding()
                .frame(width: 200, height: 150)
                .background(Rectangle().fill(Color.orange).shadow(radius: 3))
                .padding(.bottom, 30)
            
            Text(state.euroJackpotResultMain)
                .foregroundColor(.black)
                .multilineTextAlignment(.center)
                .frame(width: 200, height: 45)
                .background(Rectangle().fill(Color.white).shadow(radius: 3))
            
            Text(state.euroJackpotResultSecondary)
                .foregroundColor(.black)
                .multilineTextAlignment(.center)
                .frame(width: 200, height: 45)
                .background(Rectangle().fill(Color.white).shadow(radius: 3))
                .padding(.bottom, 20)
            
            Button("Losuj"){
                
                let mainEuroJackPot = allTogether(Set(1...50), 1...5)
                let secondaryEuroJackpot = allTogether(Set(1...10), 1...2)

                state.euroJackpotResultMain = mainEuroJackPot.map(String.init).joined(separator: ", ")
                state.euroJackpotResultSecondary = secondaryEuroJackpot.map(String.init).joined(separator: ", ")
                
            }
            
        }
        .offset(y: -40)
        .navigationBarBackButtonHidden(true)
        .navigationBarItems(leading: buttonBack)
    }
}
