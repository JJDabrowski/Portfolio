//
//  BigLottoView.swift
//  LottoSwiftUI
//
//  Created by Jakub Dąbrowski on 05/01/2022.
//

import SwiftUI
import Combine


private final class BigLottoViewState: ObservableObject {

@Published var bigLottoResult = ""
    
    
}

struct BigLottoView: View {
    
    @Environment(\.presentationMode) var presentationMode: Binding<PresentationMode>
    
    @StateObject private var state = BigLottoViewState()
    
    func iterateAndRemove() -> (Set<Int>, Set<Int>){
        var numbers = Set<Int>(1...49)
        var results = Set<Int>()
        for _ in 1...6{
            let randomNumbers = numbers.randomElement()!
            results.insert(randomNumbers)
            numbers.remove(randomNumbers)
        }
    return (numbers, results)
    }
    
    var buttonBack : some View { Button(action: {
            self.presentationMode.wrappedValue.dismiss()
            }) {
                    Text("< Powrót")
            }
        }
    
    var body: some View {
        VStack(spacing: 20){
            Text("Duży Lotek \n Chybił-trafił")
                .font(.headline)
                .foregroundColor(.blue)
                .multilineTextAlignment(.center)
                .padding()
                .frame(width: 200, height: 150)
                .background(Rectangle().fill(Color.yellow).shadow(radius: 3))
                .padding(.bottom, 30)
            
            Text(state.bigLottoResult)
                .foregroundColor(.black)
                .multilineTextAlignment(.center)
                .padding()
                .frame(width: 200, height: 80)
                .background(Rectangle().fill(Color.white).shadow(radius: 3))
                .padding(.bottom, 20)
            
            Button("Losuj"){
                
                let runFunction = iterateAndRemove()
                let result = runFunction.1
                state.bigLottoResult = result.map(String.init).joined(separator: ", ")
            
        }
        }
        .offset(y: -60)
        .navigationBarBackButtonHidden(true)
        .navigationBarItems(leading: buttonBack)
    }
}
