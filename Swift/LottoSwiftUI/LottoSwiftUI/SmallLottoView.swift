//
//  SmallLottoView.swift
//  LottoSwiftUI
//
//  Created by Jakub Dąbrowski on 05/01/2022.
//

import SwiftUI
import Combine


private final class SmallLottoViewState: ObservableObject {

@Published var smallLottoResult = ""
    
}

struct SmallLottoView: View {
    
    @Environment(\.presentationMode) var presentationMode: Binding<PresentationMode>
    
    @StateObject private var state = SmallLottoViewState()
    
    private let module = SharedModule()
    
    var buttonBack : some View { Button(action: {
            self.presentationMode.wrappedValue.dismiss()
            }) {
                    Text("< Powrót")
            }
        }
    
    var body: some View {
        
        VStack(spacing: 20){
            Text("Mały Lotek \n Chybił-trafił")
                .font(.headline)
                .foregroundColor(.green)
                .multilineTextAlignment(.center)
                .padding()
                .frame(width: 200, height: 150)
                .background(Rectangle().fill(Color.yellow).shadow(radius: 3))
                .padding(.bottom, 30)
            
            Text(state.smallLottoResult)
                .foregroundColor(.black)
                .multilineTextAlignment(.center)
                .padding()
                .frame(width: 200, height: 80)
                .background(Rectangle().fill(Color.white).shadow(radius: 3))
                .padding(.bottom, 20)
            
            Button("Losuj"){
                
                let runFunction = module.iterateAndRemove(Set(1...42), in: 1...5)
                let result = runFunction.1
                state.smallLottoResult = result.map(String.init).joined(separator: ", ")
                
            }
            
        }
        .offset(y: -60)
        .navigationBarBackButtonHidden(true)
        .navigationBarItems(leading: buttonBack)
    }
}
