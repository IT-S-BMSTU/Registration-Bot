import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from "@angular/router";
import {MainPageComponent} from "./pages/main-page/main-page.component";
import {CreationPageComponent} from "./pages/creation-page/creation-page.component";
import {ListPageComponent} from "./pages/list-page/list-page.component";
import {LoginCheckComponent} from "./login-check/login-check.component";
import {SettingsPageComponent} from "./pages/settings-page/settings-page.component";
import {TextBlockPageComponent} from "./account/text-block-page/text-block-page.component";
import {isAuthGuard} from "./guard/auth.guard";
import {BotEditPageComponent} from "./pages/bot-edit-page/bot-edit-page.component";
import {SendingPageComponent} from "./pages/sending-page/sending-page.component";

const routes: Routes = [
  {
    path: '',
    component: MainPageComponent
  },
  {
    path: 'creation',
    component: CreationPageComponent,
    canActivate: [isAuthGuard]
  },
  {
    path: 'list',
    component: ListPageComponent,
    canActivate: [isAuthGuard]
  },
  {
    path: 'settings',
    component: SettingsPageComponent,
    canActivate: [isAuthGuard]
  },
  {
    path: 'login',
    component: LoginCheckComponent
  },
  {
    path: 'add_text_block',
    component: TextBlockPageComponent,
    canActivate: [isAuthGuard]
  },
  {
    path: 'edit-bot',
    component: BotEditPageComponent
  },
  {
    path: 'sending',
    component: SendingPageComponent
  }
]

@NgModule({
  declarations: [],
  imports: [
    CommonModule, RouterModule.forRoot(routes)
  ],
  exports: [RouterModule],
})
export class AppRoutingModule { }
